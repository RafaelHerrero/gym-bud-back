from . import views
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

router = DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path("create_user/", views.create_user, name="create_user"),
    path('token/create/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
] + router.urls
