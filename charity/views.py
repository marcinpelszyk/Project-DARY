from django.shortcuts import render
from django.views.generic import TemplateView

class LandingPage(TemplateView):
    template_name = 'charity/home.html'


class AddDonation(TemplateView):
    template_name = 'charity/form.html'

class Login(TemplateView):
    template_name = 'charity/login.html'

class Register(TemplateView):
    template_name = 'charity/register.html'