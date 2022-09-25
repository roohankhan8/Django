import imp
from unicodedata import name
from django.shortcuts import render, HttpResponse
#Import Date Time
from datetime import datetime
#Import Class
from home.models import Contact
#Import Messages
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')
    # messages.success(request, 'This is success message')
    # return HttpResponse('This is response')
    # context = {
    #     'variable' : 'This is sent'
    # }
def about(request):
    return render(request, 'about.html')
    # return HttpResponse('This is about page')

def services(request):
    return render(request, 'services.html')
    # return HttpResponse('This is services page')

def contact(request):
    if request.method == 'POST':
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            number = request.POST.get('number'),
            contact = Contact(name=name, email=email, number=number, date=datetime .today())
            contact.save()
            messages.success(request, 'Profile details updated!')
    
    return render(request, 'contact.html')
    # return HttpResponse('This is contact page')
