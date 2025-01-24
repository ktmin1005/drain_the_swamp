from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Candidate

# Create your views here.candidate
def candidate_list(request):
    candidates = Candidate.objects.all()
    return render(request, 'candidates/candidate_list.html', {'candidates': candidates})

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
    
class CandidateCreateView(CreateView):
    model = Candidate
    fields = ['name', 'start_date', 'end_date']
    template_name = 'candidates/candidate_form.html'

class CandidateUpdateView(UpdateView):
    model = Candidate
    field = ['name', 'start_date', 'end_date']
    template_name = 'candidates/candidate_form.html'

class CandidateDeleteView(DeleteView):
    model = Candidate
    template_name = 'candidates/candidate_confirm_delete.html'
    success_url = reverse_lazy('candidates:candidate-list')

def search_candidates(request):
    query = request.GET.get('q', '')
    candidates = Candidate.objects.filter(name__icontains=query) if query else President.objects.all()
    return render(request, 'candidates/candidate_search.html', {'presidents': presidents, 'query': query})
#class PolicyViews()