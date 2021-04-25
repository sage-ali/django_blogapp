from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sample_view(request):
    return HttpResponse("<h1>i made a view</h1>")