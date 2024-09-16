
from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User, Profile

class UserRegisterForm(UserCreationForm):
    
    full_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Enter Full Name", 'class': "a custom class"}))
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Enter username"}))
    email = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Enter email"}))
    phone = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Enter phone"}))
    
    class Meta:
        model = User
        fields = ['full_name', 'username', 'email','phone', 'password1', 'password2']