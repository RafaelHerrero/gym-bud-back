from fastapi import APIRouter, Body, status, Response
from lib.core.workout_controller import WorkoutController
from lib.models.models import Workouts

router = APIRouter(
    prefix="/workout",
    tags=["Workout Routes"]
)

@router.get("/{user_id}/active", tags=["Workout Routes"], status_code=200, response_model=list[Workouts])
async def get_user_active_workout(user_id: str):
    workout = WorkoutController()
    return workout.get_user_active_workouts(user_id)

@router.post("/create", tags=["Workout Routes"], status_code=200)
async def create_workout(payload: list[Workouts]):
    workout = WorkoutController()
    return workout.create_workout(payload)