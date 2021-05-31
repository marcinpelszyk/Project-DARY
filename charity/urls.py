from re import L
from django.urls import path

from .views import LandingPageView, AddDonation, Login, Register

app_name = 'charity'

urlpatterns = [
    path('', LandingPageView.as_view(), name='home'),
    path('add_donation/', AddDonation.as_view(), name='add_donation'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    
]