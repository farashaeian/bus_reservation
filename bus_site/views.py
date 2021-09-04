from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.

def home(request,):
    num_buses=models.Bus.objects.all().count()
    num_users=models.User.objects.all().count()
    num_reservations=models.Book.objects.filter(status='B').count()
    return render(request, 'bus_site/home.html', context={'num_buses':num_buses, 'num_users':num_users, 'num_reservations':num_reservations})
    #return HttpResponse('welcome to home')

def login(request,):
    return HttpResponse('login to your account')

def logout(request,):
    return HttpResponse('log out from your account')

def search_reserv(request,):
    return HttpResponse('search and reserv your bus')
    
def reserv_report(request,):
    return HttpResponse('see your reservation list')

def cancel(request,):
    return HttpResponse('cancel your bus')
    
