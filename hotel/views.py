from django.shortcuts import render

from hotel.models import Hotel, Room, RoomType
from django.db.models import Min
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

def room_type_detail (request, slug, rt_slug):
    hotel = Hotel.objects.get(status="Live", slug=slug)
    room_type = RoomType.objects.get(hotel=hotel, slug=rt_slug)
    rooms = Room.objects.filter(room_type=room_type, is_available=True)
    context = {
        "hotel": hotel,
        "room_type":room_type, 
        "rooms" :rooms,
    }

    return render (request, "hotel/room_type_detail.html", context)
