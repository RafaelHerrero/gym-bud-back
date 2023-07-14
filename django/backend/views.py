from .models import Exercise, Workout, WorkoutPlan, UserWorkoutPlan, WorkoutExercise, WorkoutPlanWorkout, WorkoutSession
from .serializers import ExerciseSerializer, WorkoutSerializer, WorkoutPlanSerializer, UserWorkoutPlanSerializer, \
                         WorkoutExerciseSerializer, WorkoutSessionSerializer, WorkoutPlanWorkoutSerializer

from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema


from rest_framework.decorators import action
from rest_framework import viewsets


def index(request):
    return HttpResponse("Hello, world. You're at the GymBud Backend index.")



class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

    @action(detail=True, methods=['GET'])
    @swagger_auto_schema(
        operation_description="Get exercises for a given workout",
        operation_summary="Get exercises for a given workout",
        responses={200: ExerciseSerializer(many=True)}
    )
    def exercises(self, request, workout_id):
        workout = get_object_or_404(Workout, pk=workout_id)
        exercises = workout.exercises.all()
        data = {"exercises": []}
        for exercise in exercises:
            data["exercises"].append({
                "id": exercise.id,
                "name": exercise.name,
                "muscle_group": exercise.muscle_group,
                "description": exercise.description
            })
        return JsonResponse(data)


class WorkoutExerciseViewSet(viewsets.ModelViewSet):
    queryset = WorkoutExercise.objects.all()
    serializer_class = WorkoutExerciseSerializer

class WorkoutPlanViewSet(viewsets.ModelViewSet):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer

class UserWorkoutPlanViewSet(viewsets.ModelViewSet):
    queryset = UserWorkoutPlan.objects.all()
    serializer_class = UserWorkoutPlanSerializer

class WorkoutPlanWorkoutViewSet(viewsets.ModelViewSet):
    queryset = WorkoutPlanWorkout.objects.all()
    serializer_class = WorkoutPlanWorkoutSerializer

class WorkoutSessionViewSet(viewsets.ModelViewSet):
    queryset = WorkoutSession.objects.all()
    serializer_class = WorkoutSessionSerializer