from django.urls import path
from django.urls import admin

from .views import (
    PresidentListView,
    PresidentDetailView,
    search_presidents,
)

app_name = "presidents"
urlpatterns = [
    path('', PresidentListView.as_view(), name = 'president-list'),
    path('<int:pk>/', PresidentDetailView.as_view(), name = 'president-detail'),
    path('search/', search_presidents, name = 'president-search'),
    path("admin/", admin.site.urls),
]