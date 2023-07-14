from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


router = DefaultRouter()
router.register(r'workout', views.WorkoutViewSet)
router.register(r'workout-plan', views.WorkoutPlanViewSet)
router.register(r'user-workout-plan', views.UserWorkoutPlanViewSet)
router.register(r'exercise', views.ExerciseViewSet)
router.register(r'workout-exercise', views.WorkoutExerciseViewSet)
router.register(r'workout-plan-workouts', views.WorkoutPlanWorkoutViewSet)
router.register(r'workout-session', views.WorkoutSessionViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('token/create/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
] + router.urls

    # path('workout/<int:pk>/exercises/', views.WorkoutViewSet.as_view({'get': 'get_workout_exercises'}), name='workout_exercises'),