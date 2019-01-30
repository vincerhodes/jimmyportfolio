from django.shortcuts import render
from .models import d3


def home(request):
    d3s = d3.objects
    return render(request, 'd3/home.html', {'d3s': d3s})


def rounded_rect(request):
    return render(request, 'd3/rounded_rect.html')
