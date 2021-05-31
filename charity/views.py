from django.db.models import Sum

from django.views.generic.list import ListView
from django.shortcuts import render
from django.views.generic import TemplateView 


from .models import  Category, Institution, Dotation


class LandingPageView(View):
    template_name = 'charity/home.html'
    model = Dotation
    context_object_name = 'dotations'

    def get_queryset(self):
        data = Dotation.objects.aggregate(Sum('quantity'))
        return data

class AddDonation(TemplateView):
    template_name = 'charity/form.html'

class Login(TemplateView):
    template_name = 'registration/login.html'

class Register(TemplateView):
    template_name = 'registration/register.html'

# class InstitutionListView(ListView):
#     model =  Institution
#     queryset = Institution.objects.all().filter(qu)