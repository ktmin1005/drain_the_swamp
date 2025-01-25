from django.urls import path
from django.urls import admin

from .views import (
    CandidateListView,
    CandidateDetailView,
    CandidateCreateView,
    CandidateUpdateView,
    CandidateDeleteView,
    CampaignListView, 
    CampaignDetailView,
    search_candidates,
)

app_name = "candidates"
urlpatterns = [
    path('', CandidateListView.as_view(), name = 'candidate-list'),
    path('<int:pk>/', CandidateDetailView.as_view(), name = 'candidate-detail'),
    path('add/', CandidateCreateView.as_view(), name = 'candidate_add'),
    path('<int:pk>/edit/', CandidateUpdateView.as_view(), name = 'candidate-edit'),
    path('<int:pk>/delete/', CandidateDeleteView.as_view(), name = 'candidate-delete'),
    path('campaigns/', CampaignListView.as_view(), name = 'campaign-list'),
    path('campaigns/<int:pk>/', CampaignDetailView.as_view(), name = 'campaign-detail'),
    path('search/', search_candidates, name = 'candidate-search'),
    path("admin/", admin.site.urls),
]