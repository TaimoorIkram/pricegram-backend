from django.urls import path
from . import views, activity, auth
from api.auth import MyTokenObtainPairSerializer, MyTokenObtainPairView, RegisterUserView
from rest_framework_simplejwt.views import (
    # TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
urlpatterns = [
    # App API Routes
    path('', views.getAllRoutes),
    path('all/', views.getAllProducts, name = 'all-product'),
    path('products/', views.getProducts, name = 'filter-products'),
    path('product/<int:id>/', views.getProductById, name = 'product-by-id'),
    path('search/', views.getProducts, name = 'search'),
    path('searches/', activity.searchHistory, name = 'search-history'),
    path('view/', activity.viewHistory, name = 'view-history'),
    path('visit/', activity.visitHistory, name = 'visit-history'),
    path('favourite/', activity.favourite, name = 'favourite'),
    path('like/', activity.like, name = 'like'),

    # Auth API Routes
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token/register/', RegisterUserView.as_view(), name='register_user'),
]