from django.shortcuts import render, redirect
from picsapp.models import *

def home_page(request):
    cats = Category.objects.all()
    images = Image.objects.all()
    data = {'images': images, 'cats': cats}

    return render(request, 'home.html', data)

def category_page(request, cid):

    cats = Category.objects.all()
    category = Category.objects.get(pk=cid)
    images = Image.objects.filter(category=category)
    data = {'images': images, 'cats': cats}

    return render(request, 'home.html', data)

def home(request):
    return redirect('/home')