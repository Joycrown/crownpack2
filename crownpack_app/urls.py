from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('contact.html/', views.contact, name="contact"),
    path('about.html/', views.about, name="about"),
    path('section.html/', views.section, name="section"),
    path('login.html/', views.login, name="login"),
    path('sign-up.html/', views.sign_up, name="sign up"),
    path('full-section.html/', views.full_section, name="full section"),
    path('flexible.html/', views.flexible, name="flexible"),
    path('maintenance.html/', views.maintenance, name="maintenance"),
    path('cutting.html/', views.cutting, name="cutting"),
    path('quality.html/', views.quality, name="quality"),
    path('extrusion.html/', views.extrusion, name="extrusion"),
    path('offset.html/', views.offset, name="offset"),
  
]
