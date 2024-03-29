from django.db import models
from django.utils.translation import gettext_lazy as _
from authentication.models import CustomUser


class Exercise(models.Model):
    name = models.CharField(max_length=255, unique=True)
    muscle_group = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Exercise"
        verbose_name_plural = "Exercises"

    def __str__(self):
        return self.name


class Workout(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    exercises = models.ManyToManyField(Exercise, through='WorkoutExercise')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Workout"
        verbose_name_plural = "Workouts"

    def __str__(self):
        return self.name


class WorkoutPlan(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    workouts = models.ManyToManyField(Workout, through='WorkoutPlanWorkout')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Workout Plan"
        verbose_name_plural = "Workout Plan"

    def __str__(self):
        return self.name


class UserWorkoutPlan(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    started_at = models.DateTimeField(null=True, blank=True)
    finished_at = models.DateTimeField(null=True, blank=True)
    expected_duration = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "User Workout Plan"
        verbose_name_plural = "User Workout Plan"

    def __str__(self):
        return f"{self.user.first_name} - {self.workout_plan.name}"


class WorkoutExercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    reps = models.IntegerField()
    sets = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Workout Exercise"
        verbose_name_plural = "Workout Exercise"

    def __str__(self):
        return f"{self.workout.name} - {self.exercise.name}"


class WorkoutPlanWorkout(models.Model):
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Workout Plan Workout"
        verbose_name_plural = "Workout Plan Workout"

    def __str__(self):
        return f"{self.workout_plan.name} - {self.workout.name}"


class WorkoutSession(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    workout_plan = models.ForeignKey('WorkoutPlan', on_delete=models.CASCADE)
    workout = models.ForeignKey('Workout', on_delete=models.CASCADE)
    exercise = models.ForeignKey('Exercise', on_delete=models.CASCADE)
    set_number = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Workout Session'
        verbose_name_plural = 'Workout Sessions'

    def __str__(self):
        return f"{self.user.first_name} - {self.workout.name} - {self.exercise.name}"
