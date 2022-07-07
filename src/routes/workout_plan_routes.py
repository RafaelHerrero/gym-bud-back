from fastapi import APIRouter, Body, status, Response
from lib.core.workout_plan_controller import WorkoutPlanController

router = APIRouter(
    prefix="/workout_plan",
    tags=["Workout Plan Routes"]
)

@router.get("/all", tags=["Workout Plan Routes"], status_code=200)
async def get_all_workout_plans():
    workout = WorkoutPlanController()
    return workout.get_all_workout_plans()

@router.get("/active/{user_id}", tags=["Workout Plan Routes"], status_code=200)
async def get_user_active_workout_plans(user_id):
    workout = WorkoutPlanController()
    return workout.get_user_active_workout_plans(user_id)
