from django.shortcuts import render

from hotel.models import Hotel
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

