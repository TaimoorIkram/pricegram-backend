from django.urls import path
from . import views

urlpatterns = [
    path('', views.getAllItems),
    path('add/', views.addPerson),
    path('products/', views.getProducts, name = 'products'),
    path('product/<int:id>/', views.getProduct, name = 'product'),
]