from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('contact.html/', views.contact, name="contact"),
    path('about.html/', views.about, name="about"),
    path('section.html/', views.section, name="section"),
    path('food.html/', views.food, name="food"),
    path('quality.html/', views.quality, name="quality"),
  
]
