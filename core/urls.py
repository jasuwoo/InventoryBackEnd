from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView
from .views import UserView
from django.contrib import admin
from django.urls import path
from contents.views import ContentView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/contents/' , ContentView.as_view() ),
    path('api/auth/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/auth/users/', UserView.as_view()),
]
