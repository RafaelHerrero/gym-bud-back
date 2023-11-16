from django.urls import path
# from rest_framework.routers import DefaultRouter
from . import views

# router = DefaultRouter()
# router.register(r'workout', views.WorkoutViewSet)

urlpatterns = [
    path('', views.index, name='client_index'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('home/', views.home, name='home')
]
