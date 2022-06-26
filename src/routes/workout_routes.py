from fastapi import APIRouter, Body, status, Response
from lib.core.workout_rules import WorkoutService
from lib.models.models import Workouts

router = APIRouter(
    prefix="/workout",
    tags=["Workout Routes"]
)

@router.get("/{user_id}/active", tags=["Workout Routes"], status_code=200, response_model=list[Workouts])
async def get_user_active_workout(user_id: str):
    workout = WorkoutService()
    return workout.get_user_active_workout(user_id)

@router.get("/workout_plans/all", tags=["Workout Routes"], status_code=200)
async def get_all_workout_plans():
    workout = WorkoutService()
    return workout.get_all_workout_plans()

@router.get("/workout_plans/active/{user_id}", tags=["Workout Routes"], status_code=200)
async def get_user_active_workout_plans(user_id):
    workout = WorkoutService()
    return workout.get_user_active_workout_plans(user_id)