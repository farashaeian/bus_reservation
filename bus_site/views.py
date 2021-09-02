from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.

def home(request,):
    return HttpResponse('welcome to home')

def login(request,):
    return HttpResponse('login to your account')

def logout(request,):
    return HttpResponse('log out from your account')

def search_reserv(request,):
    x=models.Bus.objects.order_by('source')
    context={'bus_list':x}
    return render(request, 'bus_site/home.html', context)
def reserv_report(request,):
    return HttpResponse('see your reservation list')

def cancel(request,):
    return HttpResponse('cancel your bus')
    
