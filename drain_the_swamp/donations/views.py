from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Donation
# Create your views here

class DonationListView(ListView):
    model = Donation
    template_name = 'donations/donation_list.html'
    context_object_name = 'donations'

class DonationDetailView(DetailView):
    model = Donation
    template_name = 'donations/donation_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        donation = self.get_object()
        context['recipient'] = donation.recipient
        return context
