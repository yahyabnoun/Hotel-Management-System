from django.shortcuts import render
from django.db import models

from hotel.models import Booking

# Create your views here.


def dashboard (request):

    bookings = Booking.objects.filter(user=request.user, payment_status="paid")
    total_spent = Booking.objects.filter(user=request.user, payment_status="paid").aggregate(amount=models.Sum("total"))
    
    context = {
        "bookings": bookings,
        "total_spent": total_spent,
    }

    return render(request, "user_dashboard/dashboard.html", context)

