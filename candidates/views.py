from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Candidate, Campaign

# Create your views here.

def candidate_list(request):
    candidates = Candidate.objects.all()
    return render(request, 'candidatess/candidate_list.html', {'candidates': candidates})

class CandidateListView(ListView):
    model = Candidate
    template_name = "/candidates/candidate_list.html"
    context_object_name = 'candidates'

class CandidateDetailView(DetailView):
    model = Candidate
    template_name = '/candidates/candidate_detail.html'
    context_object_name = 'candidate'

    '''def get_context_data(self, **kwards):
        context = super().get_context_data(**kwards)
        context['donations'] = self.object.donation_set.all()
        context['endorsed_policies'] = self.object.policies_endorsed.all()
        context['enacted_policies'] = self.object.policies_enacted.all()
        context['vetoed_policies'] = self.object.policies_vetoed.all()
        return context'''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['campaigns'] = self.object.campaigns.all()
        return context

class CampaignListView(ListView):
    model = Campaign
    template_name = 'candidates/campaign_list.html'
    context_object_name = 'campaigns'

class CampaignDetailView(DetailView):
    model = Campaign
    template_name = 'candidates/campaign_detail.html'
    
class CandidateCreateView(CreateView):
    model = Candidate
    fields = ['name', 'party', 'position', 'start_date', 'end_date', 'incumbent']
    template_name = 'candidates/candidate_form.html'

class CandidateUpdateView(UpdateView):
    model = Candidate
    fields = ['name', 'party', 'position', 'start_date', 'end_date', 'incumbent']
    template_name = 'candidates/candidate_form.html'

class CandidateDeleteView(DeleteView):
    model = Candidate
    template_name = 'candidates/candidate_confirm_delete.html'
    success_url = reverse_lazy('candidates:candidate-list')

def search_candidates(request):
    query = request.GET.get('q', '')
    candidates = Candidate.objects.filter(name_icontains = query) if query else Candidate.objects.all()
    return render(request, 'candidates/candidate_search.html', {'candidates': candidates, 'query': query})
    