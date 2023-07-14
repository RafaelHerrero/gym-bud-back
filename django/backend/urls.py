from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views


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
] + router.urls

    # path('workout/<int:pk>/exercises/', views.WorkoutViewSet.as_view({'get': 'get_workout_exercises'}), name='workout_exercises'),