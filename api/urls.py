from django.urls import path
from . import views

urlpatterns = [
    path('', views.getAllRoutes),
    path('products/', views.getProducts, name = 'products'),
    path('product/<int:id>/', views.getProduct, name = 'product'),
    path('all/', views.getAllProducts, name = 'product'),
]