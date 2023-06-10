from django.urls import path
from . import views
from api.views import MyTokenObtainPairSerializer, MyTokenObtainPairView, RegisterUserView
from rest_framework_simplejwt.views import (
    # TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
urlpatterns = [
    path('', views.getAllRoutes),
    path('all/', views.getAllProducts, name = 'all-product'),
    path('products/', views.getProducts, name = 'filter-products'),
    path('product/<int:id>/', views.getProductById, name = 'product-by-id'),
    path('search/', views.getProductById, name = 'search-history'),
    path('view/', views.getProductById, name = 'view-history'),
    path('visit/', views.getProductById, name = 'visit-history'),
    path('favourite/', views.getProductById, name = 'favourites'),

    # auth simplejwt
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token/register/', RegisterUserView.as_view(), name='register_user'),
]