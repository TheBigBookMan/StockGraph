from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Favourites

# Create your views here.

def index(response, id):
  ls = User.objects.get(id=id)
  items= ls.favourites_set.get(id=1)
  return HttpResponse(f"""<h1>StockGraph</h1>
  <h3>{ls.name}</h3>
  <p>{items.ticker}</p>""")

def stock_page(response):
  return HttpResponse("<h1>Apple</h1>")