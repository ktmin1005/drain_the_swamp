from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Donor
# Create your views here.
class DonorListView(ListView):
    model = Donor
    template_name = 'donors/donor_list.html'
    context_object_name = 'donors'

class DonorDetailView(DetailView):
    model = Donor
    template_name = 'donors/donor_detail.html'