from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html', {})


def contact(request):
    if request.method == "POST":
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
         

        send_mail(f_name, message, email, ['olaniyanayoade@ymail.com'],)
        return render(request, 'contact.html', {})

    else:
        return render(request, 'contact.html', {})


def about(request):
    return render(request, 'about.html', {})



def section(request):
    return render(request, 'section.html', {}) 



def login(request):
    return render(request, 'login.html', {}) 


def sign_up(request):
    return render(request, 'sign-up.html', {})


def full_section(request):
    return render(request, 'full-section.html', {}) 


def flexible(request):
    return render(request, 'flexible.html', {})


def offset(request):
    return render(request, 'offset.html', {})     


def quality(request):
    return render(request, 'quality.html', {}) 


def maintenance(request):
    return render(request, 'maintenance.html', {})      


def extrusion(request):
    return render(request, 'extrusion.html', {})   


def cutting(request):
    return render(request, 'cutting.html', {})                                    