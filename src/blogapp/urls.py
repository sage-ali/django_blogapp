from django.urls import path
from . import views

urlpatterns = [
    path('', views.sample_view, name = 'sample'),
]