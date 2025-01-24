from django.urls import path, include
from django.contrib import admin

from .views import DonationListView, DonationDetailView

urlpatterns = [
    path('', DonationListView.as_view(), name = 'donation-list'),
    path('<int:pk>/', DonationDetailView.as_view(), name= 'donation-detail'),
    path("admin/", admin.site.urls),
]