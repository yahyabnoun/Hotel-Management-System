from django.urls import path
from hotel import views

app_name = "hotel"

urlpatterns = [
    path("", views.index, name="index"),
    path("detail/<slug>/", views.hotel_detail, name="hotel_detail")
]


