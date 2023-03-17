from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path("exercise/", views.ExerciseList.as_view(),name="exercise_list"),
    path("exercise/<int:pk>/", views.ExerciseDetail.as_view(),name="exercise_detail"),

    path("workout/",views.WorkoutsList.as_view(),name="workout_list"),
    path("workout/<int:pk>/",views.WorkoutsDetail.as_view(),name="workout_detail"),

    path("workout-exercise/",views.WorkoutExercisesList.as_view(),name="workout_exercise_list"),
    path("workout-exercise/<int:pk>/",views.WorkoutExercisesDetail.as_view(),name="workout_exercise_list"),

    path("workout-plan/",views.WorkoutPlansList.as_view(),name="workout_plans_list"),
    path("workout-plan/<int:pk>/",views.WorkoutPlansDetail.as_view(),name="workout_plans_detail"),

    path("user-workout-plan/",views.UserWorkoutPlansList.as_view(),name="user_workout_plans_list"),
    path("user-workout-plan/<int:pk>/",views.UserWorkoutPlansDetail.as_view(),name="user_workout_plans_detail"),

    path("workout-plan-workouts/",views.WorkoutPlanWorkoutsList.as_view(),name="workout_plans_workout_list"),
    path("workout-plan-workouts/<int:pk>/",views.WorkoutPlanWorkoutsDetail.as_view(),name="workout_plans_workout_detail"),

    path("workout-session/",views.WorkoutSessionList.as_view(),name="workout_session_list"),
    path("workout-session/<int:pk>/",views.WorkoutSessionDetail.as_view(),name="workout_session_detail"),
]
