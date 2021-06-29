from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def about(request):
    return render(request, 'about.html', {})



def section(request):
    return render(request, 'section.html', {}) 



def quality(request):
    return render(request, 'quality.html', {}) 


def food(request):
    return render(request, 'food.html', {})           