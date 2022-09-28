from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.create_user),
    path('register-login/', views.create_user_with_login),
    path('login/', views.login_user),
    path('logout/', views.logout_user),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
