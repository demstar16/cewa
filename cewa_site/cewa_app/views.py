from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "home.html")

def products(request):
    return render(request, "products.html")

def services(request):
    return render(request, "services.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")