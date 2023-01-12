from django.urls import path

from . import views

urlpatterns = [
  path("<int:id>", views.index, name="index"),


  path("stock/", views.stock_page, name="stock")
]