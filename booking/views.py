from django.shortcuts import render

from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from hotel.models import Hotel, RoomType

# Create your views here.

def check_room_availability(request): 
    if request.method == "POST":
        id = request.POST.get("hotel-id") 
        checkin = request.POST.get("checkin") 
        checkout = request.POST.get("checkout") 
        adult = request.POST.get("adult") 
        children = request.POST.get("children")
        room_type = request.POST.get("room_type")
        hotel = Hotel.objects.get(id=id)
        room_type = RoomType.objects.get(hotel=hotel, slug=room_type)
        
        # print("id =====", id)
        # print("checkin =====", checkin)
        # print("checkout =====", checkout)
        # print("adult =====", adult) 
        # print("children =====", children) 
        # print("room_type =====", room_type.slug) 
        # print("hotel =====", hotel)

        # return JsonResponse({"available": children})  # Example response
    
    
        url = reverse("hotel:room_type_detail", args=[hotel.slug, room_type.slug])
        url_with_params = f"{url}?hotel-id={id}&checkin={checkin}&checkout={checkout}&adult={adult}&children={children}&r"
        return HttpResponseRedirect(url_with_params)