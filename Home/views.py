from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

# welcome
def welcome(request):
    template = loader.get_template('pages/welcome.html')
    return HttpResponse(template.render())

# index
@login_required(login_url='/signin/')
def index(request):
    template = loader.get_template('pages/home.html')
    return HttpResponse(template.render())