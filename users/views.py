from django.shortcuts import render
from .form import CustomUserForm
from .models import MyUser
from django.views.generic import CreateView


# Create your views here.
class SignUpView(CreateView):
    model = MyUser
    form_class = CustomUserForm
    success_url = 'success.html'
    template_name = 'signup.html'
