
from django.urls import path
from hotel import views


app_name = "hotel"

urlpatterns = [
    path("", views.index, name="index")

]


