from django.urls import path 
from user_dashboard import views

app_name = "user_dashboard"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
]