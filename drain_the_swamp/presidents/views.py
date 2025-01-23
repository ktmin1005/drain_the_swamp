from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import President

# Create your views here.

def president_list(request):
    presidents = President.objects.all()
    return render(request, 'presidents/president_list.html', {'presidents': presidents})

class PresidentListView(ListView):
    model = President
    template_name = "/presidents/president_list.html"
    context_object_name = 'presidents'

class PresidentDetailView(DetailView):
    model = President
    template_name = '/presidents/president_detail.html'
    context_object_name = 'president'
    
    '''def get_context_data(self, **kwards):
        context = super().get_context_data(**kwards)
        context['donations'] = self.object.donation_set.all()
        context['endorsed_policies'] = self.object.policies_endorsed.all()
        context['enacted_policies'] = self.object.policies_enacted.all()
        context['vetoed_policies'] = self.object.policies_vetoed.all()
        return context'''
    
class PresidentCreateView(CreateView):
    model = President
    fields = ['name', 'start_date', 'end_date']
    template_name = 'presidents/president_form.html'

class PresidentUpdateView(UpdateView):
    model = President
    field = ['name', 'start_date', 'end_date']
    template_name = 'presidents/president_form.html'

class PresidentDeleteView(DeleteView):
    model = President
    template_name = 'presidents/president_confirm_delete.html'
    success_url = reverse_lazy('presidents:president-list')

def search_presidents(request):
    query = request.GET.get('q', '')
    presidents = President.objects.filter(name__icontains=query) if query else President.objects.all()
    return render(request, 'presidents/president_search.html', {'presidents': presidents, 'query': query})
#class PolicyViews()