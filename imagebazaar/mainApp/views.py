from django.shortcuts import render
from .models import *

def home(request):
    cats = Category.objects.all().order_by("title")
    myimages = Image.objects.all().order_by("-id")
    return render(request,"index.html",{'myimages': myimages, "cats": cats})

def category(request,cid):
    cats = Category.objects.all()

    category = Category.objects.get(pk=cid)

    myimages = Image.objects.filter(cat=category).order_by("-id")
    return render(request,"index.html",{'myimages': myimages, 'cats': cats})

