from django.contrib import admin

from .models import Exercise, Workout, WorkoutPlan, UserWorkoutPlan, WorkoutExercise, WorkoutPlanWorkout, CustomUser

admin.site.register(CustomUser)
admin.site.register(Exercise)
admin.site.register(Workout)
admin.site.register(WorkoutPlan)
admin.site.register(UserWorkoutPlan)
admin.site.register(WorkoutExercise)
admin.site.register(WorkoutPlanWorkout)
