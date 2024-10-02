from datetime import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from flask import redirect
from django.contrib import messages

from hotel.models import Booking, Hotel, Room, RoomType
from django.db.models import Min
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    hotels = Hotel.objects.filter(status="Live").annotate(lowest_price=Min('roomtype__price'))
    context = {"hotels": hotels
    }
    return render(request, "hotel/hotel.html", context)


def hotel_detail(request, slug):
    hotel = Hotel.objects.get(status="Live", slug=slug)
    context = {
        "hotel": hotel
     }
    return render (request, "hotel/hotel_detail.html", context)

def room_type_detail(request, slug, rt_slug):
    hotel = Hotel.objects.get(status="Live", slug=slug)
    room_type = RoomType.objects.get(hotel=hotel, slug=rt_slug)
    rooms = Room.objects.filter(room_type=room_type, is_available=True)
    
    
    # Capture the parameters from the URL
    checkin = request.GET.get('checkin')
    checkout = request.GET.get('checkout')
    adult = request.GET.get('adult')
    children = request.GET.get('children')
    

    context = {
        "hotel": hotel,
        "room_type":room_type, 
        "rooms" :rooms,
        'checkin': checkin,
        'checkout': checkout,
        'adult': adult,
        'children': children
    }

    return render(request, "hotel/room_type_detail.html", context)


# def selected_rooms(request):
    # total = 0
    # room_count = 0
    # total_days= 0
    # adult = 0
    # children = 0
    # checkin = ""
    # checkout = ""
    
    
    # if request.method == "POST":
        # print(request)
        
        # id = int(item['hotel_id']) 
        # checkin = item['checkin'] 
        # checkout = item['checkout'] 
        # adult = int(item['adult']) 
        # children = int(item['children']) 
        # room_type = int(item['room_type']) 
        # room_id= int(item['room_id'])
        # hotel = None
        
        
        
        # room_type = RoomType.objects.get(id=room_type_)
        # date_format = "%Y-%m-%d"
        # checkin_date = datetime.strptime(checkin, date_format) 
        # checkout_date = datetime. strptime (checkout, date_format) time_diffrence = checkout_date
        # -
        # total_days time_diffrence.days
        # room_count += 1
        # days = total_days
        # price = room_type.price
        # checkin_date
        # room_price = price room_count # 20 3 = 60
        # total = room_price* days
        # hotel Hotel.objects.get(id=id)
        # =


def checkout(request):

    if request.user.is_authenticated:
        if request.method == 'POST':
            room_id = request.POST.get('room_id')
            checkin = request.POST.get('checkin')
            hotel_id = request.POST.get('hotel-id')
            room_type_id = request.POST.get('room_type')
            checkout = request.POST.get('checkout')
            adult = request.POST.get('adult')
            children = request.POST.get('children')
            
            hotelPost = Hotel.objects.get(id=hotel_id)
            roomPost = Room.objects.get(id=room_id)
            room_typePost = RoomType.objects.get(id=room_type_id)
        

            # Check if the user already has a booking for the same room type and date
            existing_booking = Booking.objects.filter(
                user=request.user,
                room_type=room_typePost,
                check_in_date=checkin,
                check_out_date=checkout
            ).exists()

            if existing_booking:
                messages.error(request, 'You already have a booking for this room type on these dates.')
                next = request.POST.get('next', '/checkout')
                return HttpResponseRedirect(next)



            
            date_format = "%Y-%m-%d"
            checkin_date = datetime.strptime(checkin, date_format).date()
            checkout_date = datetime.strptime(checkout, date_format).date()

            totaldays = (checkout_date - checkin_date).days
            if totaldays == 0 :
                totaldays = 1
            
            TotalPrieroomtype = room_typePost.price * totaldays


            booking = Booking.objects.create(
                user=request.user,
                hotel=hotelPost,
                room_type=room_typePost,
                check_in_date=checkin,
                check_out_date=checkout,
                               num_adults=adult,
                num_children=children,
                total_days = totaldays,
                total = TotalPrieroomtype,
            )

            # Use the set() method to assign the room
            booking.room.set([roomPost])

            booking.save()


            messages.success(request, 'Booking created successfully!')

    
        try:
            user = request.user

            # Check if the user has bookings
            booking = Booking.objects.filter(user=user,payment_status='pending')
            
            TOTAL = 0
            
            for x in booking:
                TOTAL += x.total
            
            
            context = {
                "booking": booking,
                "TOTAL": TOTAL,
            }
            
            
            
            
            return render(request, "hotel/checkout.html", context)
        except Booking.DoesNotExist:
            # Redirect or show a message if the user doesn't have any booking
            return render(request, "hotel/checkout.html")  # Or show a custom message/page

    # Redirect unauthenticated users to the sign-up page
    next = request.POST.get('next', '/user/sign-in/')
    return HttpResponseRedirect(next)

    
def deleteFromcheckout(request,booking_id):
    
    booking = Booking.objects.filter(user=request.user,id=booking_id,payment_status='pending').delete()
    messages.success(request, 'Booking deleted successfully!')
    
    next = request.POST.get('next', '/checkout/')
    return HttpResponseRedirect(next)


@login_required
def successPayment(request):
    if request.method == 'POST':
        # Get data from the POST request
        fullName = request.POST.get('fullName')
        Email = request.POST.get('Email')
        Phone = request.POST.get('Phone')
        
        booking = Booking.objects.filter(user=request.user, payment_status='pending')

        TOTAL = 0
        for bok in booking:
            TOTAL = bok.room_type.price
            bok.payment_status = 'paid'
            bok.full_name = fullName
            bok.email = Email
            bok.phone = Phone
            bok.total = TOTAL
            bok.save()
        
        # Return success response to the frontend
        return JsonResponse({'status': 'success'})
    
    return render(request, "hotel/successPayment.html")
        
    
        
    