from importlib.util import resolve_name
from django.shortcuts import render

# Create your views here.

def new(request):
    return render(request,'corona.html')