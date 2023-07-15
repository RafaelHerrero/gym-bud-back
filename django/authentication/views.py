import json
from .models import CustomUser, LoginHistory
from rest_framework import viewsets
from .serializer import UserSerializer
from django.contrib.auth import get_user_model
from django.http import HttpResponse, JsonResponse
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response

def index(request):
    return HttpResponse("Hello, world. You're at the GymBud Auth index.")

@csrf_exempt
def register(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        User = get_user_model()
        try:
            user = User.objects.register(body=body)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

        return JsonResponse({'success': 'User created successfully', "user_id": str(user.id)}, status=201)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


class CustomLoginView(TokenObtainPairView):
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.user
        LoginHistory.objects.create(user=user)
        data = response.data
        data['user_id'] = str(user.id)
        return Response(data)


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
