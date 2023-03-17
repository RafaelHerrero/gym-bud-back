from rest_framework import serializers
from .models import Exercise, Workout, WorkoutPlan, UserWorkoutPlan, WorkoutExercise, WorkoutSession, WorkoutPlanWorkout


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'


class WorkoutPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutPlan
        fields = '__all__'


class UserWorkoutPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWorkoutPlan
        fields = '__all__'


class WorkoutExerciseSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer(many=False, read_only=True)

    class Meta:
        model = WorkoutExercise
        fields = '__all__'


class WorkoutSessionSerializer(serializers.ModelSerializer):
    workout_exercise = WorkoutExerciseSerializer(many=False, read_only=True)

    class Meta:
        model = WorkoutSession
        fields = '__all__'


class WorkoutPlanWorkoutSerializer(serializers.ModelSerializer):
    workout_plan = WorkoutPlanSerializer(read_only=True)
    workout = WorkoutSerializer(read_only=True)

    class Meta:
        model = WorkoutPlanWorkout
        fields = '__all__'

