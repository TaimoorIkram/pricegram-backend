from django.urls import path
from .views import products, activity, auth
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)
urlpatterns = [
    # App API Routes
    path('', products.getAllRoutes),
    path('all/', products.getAllProducts, name = 'all-product'),
    path('products/', products.getProducts, name = 'filter-products'),
    path('product/<int:id>/', products.getProductById, name = 'product-by-id'),
    path('search/', products.getProducts, name = 'search'),
    path('searches/', activity.searchHistory, name = 'search-history'),
    path('view/', activity.viewHistory, name = 'view-history'),
    path('visit/', activity.visitHistory, name = 'visit-history'),
    path('favourite/', activity.favourite, name = 'favourite'),
    path('like/', activity.like, name = 'like'),

    # Auth API Routes
    path('token/', auth.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token/register/', auth.RegisterUserView.as_view(), name='register_user'),
]