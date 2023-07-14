import json
from .models import CustomUser
from rest_framework import viewsets
from .serializer import UserSerializer
from django.contrib.auth import get_user_model
from django.http import HttpResponse, JsonResponse
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return HttpResponse("Hello, world. You're at the GymBud Auth index.")

@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        User = get_user_model()
        try:
            User.objects.create_user(body=body)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

        return JsonResponse({'success': 'User created successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

class LoginView(TokenObtainPairView):
    permission_classes = [AllowAny]


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
