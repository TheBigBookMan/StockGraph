from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Favourites

# Create your views here.

def index(response, id):
  ls = User.objects.get(id=id)
  items= ls.favourites_set.get(id=1)
  my_dict = {
    "name": ls.name,
    "favourites": items.ticker
  }
  return render(response, "main/base.html", my_dict)

def stock_page(response):
  return HttpResponse("<h1>Apple</h1>")

def home(response):
  return render(response, "main/home.html", {})

