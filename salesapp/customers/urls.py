from .views import DashboardTemplateView
from django.urls import path

urlpatterns = [
    path('', DashboardTemplateView.as_view()),
]
