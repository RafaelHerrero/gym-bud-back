
from fastapi import APIRouter, Body, status, Response
from lib.core.exercise_controller import ExerciseController
from lib.models.models import Workouts

router = APIRouter(
    prefix="/exercises",
    tags=["Exercises Routes"]
)

@router.get("/{workout_id}/{user_id}", tags=["Exercises Routes"], status_code=200)
async def get_exercises_from_workout(user_id: str, workout_id: str):
    exercises = ExerciseController()
    return exercises.get_exercises_from_workout()

@router.get("/{muscle_group}", tags=["Exercises Routes"], status_code=200)
async def get_exercise_by_muscle_group(muscle_group: str):
    exercises = ExerciseController()
    return exercises.get_exercise_by_muscle_group()
