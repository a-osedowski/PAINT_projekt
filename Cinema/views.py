from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def cennik(request):
    return render(request, 'cennik.html')
