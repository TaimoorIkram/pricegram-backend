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
    path('search/', products.search, name = 'search'),
    path('searches/', activity.searchHistory, name = 'search-history'),
    path('view/', activity.viewHistory, name = 'view-history'),
    path('visit/', activity.visitHistory, name = 'visit-history'),
    path('favourite/', activity.favourite, name = 'favourite'),
    path('unitfavourite/<int:id>', activity.unitFavourite, name = 'specific-favourite'),
    path('rmvfavourite/<int:id>', activity.removeFromFavourites, name = 'remove-from-favourites'),
    path('like/', activity.like, name = 'like'),
    path('unitlike/<int:id>', activity.unitLike, name = 'specific-like'),
    path('unlike/<int:id>', activity.unlike, name = 'unlike'),
    path('review/', activity.insertReview, name = 'add-review'),
    path('feedback/', activity.insertFeedback, name = 'add-feedback'),
    path('feedbacks/', activity.getFeedback, name = 'get-feedback'),
    path('matchuser/', activity.matchUser, name = 'match-user'),
    
    # Auth API Routes
    path('token/', auth.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token/register/', auth.RegisterUserView.as_view(), name='register_user'),
]