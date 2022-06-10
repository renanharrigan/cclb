from django.urls import path 
from . import views 

app_name = "cclbapp"

urlpatterns = [
   path('', views.index, name='index'),
   path('howtograb', views.howtograb, name='howtograb'),
   path('properties', views.properties, name='properties'),
   path("register", views.register_request, name="register"),
   path("login", views.login_request, name="login"),
   path("logout", views.logout_request, name= "logout"),
]
   