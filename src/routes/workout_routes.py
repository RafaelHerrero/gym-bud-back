from fastapi import APIRouter, Body, status, Response
from lib.core.workout_rules import WorkoutService

router = APIRouter(
    prefix="/workout",
    tags=["Workout Routes"]
)

@router.get("/{user_id}/active", tags=["Workout Routes"], status_code=200)
async def get_user_active_workout(user_id: str):
    workout = WorkoutService()
    return workout.get_user_active_workout(user_id)

@router.get("/workout_plans/all", tags=["Workout Routes"], status_code=200)
async def get_all_workout_plans():
    workout = WorkoutService()
    return workout.get_all_workout_plans()
