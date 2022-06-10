import re
import googlemaps
import simplekml
import pandas
import requests
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    
    API_KEY = 'AIzaSyDaG1DJvvM8hq1mufzM4RI1tVDAGItwki0'

    gmaps = googlemaps.Client(API_KEY)
    
      
    return render(request, 'cclbapp/index.html')

def howtograb(request):
    return render(request, "cclbapp/howtograb.html")
def properties(request):
    return render(request, "cclbapp/properties.html")

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("cclbapp:index")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="cclbapp/register.html", context={"register_form":form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("cclbapp:index")
            else:
                messages.error(request,"Invalid username or password.")
    else:
        messages.error(request,"Invalid username or password.")
        form = AuthenticationForm()
    return render(request=request, template_name="cclbapp/login.html", context={"login_form":form})     

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect("cclbapp:index")   
   

# cclb =input("cclb: ")   
# data = csv.reader(open('cclb.csv'), delimiter= ',')
# kml = simplekml.Kml()

# f = open('csv2kml.kml', 'w')

# response = request.get("https://www.google.com/maps/d/u/1/edit?mid=1OGUQrsxmK96d7F78A-oQLIgtzBalSuDE&ll=33.52536647831128%2C-84.3528385&z=12")
