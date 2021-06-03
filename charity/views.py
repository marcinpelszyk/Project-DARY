from django.db import models
from django.db.models import Sum
from django.db.models.aggregates import Count

from django.views.generic.list import ListView
from django.shortcuts import render
from django.views.generic import TemplateView 


from .models import  Category, Institution, Dotation


class LandingPageView(ListView):
    template_name = 'charity/home.html'
    paginate_by = 10
    model = Institution
    
    


    

   



    
    
    

# class LandingPageView(ListView):
#     template_name = 'charity/home.html'
#     context_object_name = 'institutions'
#     paginate_by = 3

class AddDonation(TemplateView):
    template_name = 'charity/form.html'

class Login(TemplateView):
    template_name = 'registration/login.html'

class Register(TemplateView):
    template_name = 'registration/register.html'

# class InstitutionListView(ListView):
#     model =  Institution
#     queryset = Institution.objects.all().filter(qu)