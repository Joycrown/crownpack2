from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {})


def contact(request):
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