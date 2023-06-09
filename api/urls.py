from django.urls import path
from . import views

urlpatterns = [
    path('', views.getAllRoutes),
    path('all/', views.getAllProducts, name = 'all-product'),
    path('products/', views.getProducts, name = 'filter-products'),
    path('product/<int:id>/', views.getProductById, name = 'product-by-id'),
    path('search/', views.getProductById, name = 'search-history'),
    path('view/', views.getProductById, name = 'view-history'),
    path('visit/', views.getProductById, name = 'visit-history'),
    path('favourite/', views.getProductById, name = 'favourites'),
]