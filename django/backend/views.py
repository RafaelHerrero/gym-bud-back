from django.shortcuts import render

from django.http import HttpResponse
from rest_framework import generics
from .models import Exercise, Workout, WorkoutPlan, UserWorkoutPlan, WorkoutExercise, WorkoutPlanWorkout, WorkoutSession
from .serializers import ExerciseSerializer, WorkoutSerializer, WorkoutPlanSerializer, UserWorkoutPlanSerializer, WorkoutExerciseSerializer, WorkoutSessionSerializer, WorkoutPlanWorkoutSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class ExerciseList(generics.ListCreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class ExerciseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class WorkoutsList(generics.ListCreateAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer


class WorkoutsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer


class WorkoutExercisesList(generics.ListCreateAPIView):
    queryset = WorkoutExercise.objects.all()
    serializer_class = WorkoutExerciseSerializer


class WorkoutExercisesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkoutExercise.objects.all()
    serializer_class = WorkoutExerciseSerializer


class WorkoutPlansList(generics.ListCreateAPIView):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer


class WorkoutPlansDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer


class UserWorkoutPlansList(generics.ListCreateAPIView):
    queryset = UserWorkoutPlan.objects.all()
    serializer_class = UserWorkoutPlanSerializer


class UserWorkoutPlansDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserWorkoutPlan.objects.all()
    serializer_class = UserWorkoutPlanSerializer


class WorkoutPlanWorkoutsList(generics.ListCreateAPIView):
    queryset = WorkoutPlanWorkout.objects.all()
    serializer_class = WorkoutPlanWorkoutSerializer


class WorkoutPlanWorkoutsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkoutPlanWorkout.objects.all()
    serializer_class = WorkoutPlanWorkoutSerializer


class WorkoutSessionList(generics.ListCreateAPIView):
    queryset = WorkoutSession.objects.all()
    serializer_class = WorkoutSessionSerializer


class WorkoutSessionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkoutSession.objects.all()
    serializer_class = WorkoutSessionSerializer
