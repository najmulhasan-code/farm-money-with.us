from django.contrib import admin
from django.urls import path
from .views import FarmingDecisionView, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('farming-decision/', FarmingDecisionView.as_view(), name='farming-decision'),
    path('farming-decision/<str:step>/', FarmingDecisionView.as_view(), name='farming-step-decision'),
]
