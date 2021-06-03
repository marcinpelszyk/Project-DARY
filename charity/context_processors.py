# from django.db.models import Sum

# from django.shortcuts import render, get_object_or_404
# from .models import Dotation, Institution


# def quantityBags(request):
#     return Dotation.objects.annotate(quantity=Sum(request.GET))

from django.db.models import Count, Q

from .models import Institution, Dotation


def quantity_bags(request):
    return {
        'quantity_bags': Dotation.objects.all().values_list("quantity").count()
    }

def institution_qty(request):
    return {
        'institution_qty': Institution.objects.count(),
        'fundations': Institution.fundations.all(),
        'organizations': Institution.organization.all(),
        'locals': Institution.local.all(),
        
    }
