from django.http import HttpResponse
from .serializer import UserSerializer
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny


def index(request):
    return HttpResponse("Hello, world. You're at the GymBud Auth index.")

class LoginView(TokenObtainPairView):
    permission_classes = [AllowAny]


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer