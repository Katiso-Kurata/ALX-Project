from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import ReviewViewSet, UserCreateView
from . import views
#JWT authentication

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('users/', UserCreateView.as_view(), name='user-create'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('reviews/', views.ReviewList.as_view(), name='review-list'),
]



urlpatterns += router.urls



