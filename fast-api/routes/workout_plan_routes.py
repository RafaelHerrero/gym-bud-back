from fastapi import APIRouter, Body, status, Response
from lib.core.workout_plan_controller import WorkoutPlanController
from lib.models.models import WorkoutPlan, DeleteWorkoutPlan

router = APIRouter(
    prefix="/workout_plan",
    tags=["Workout Plan Routes"]
)

@router.get("/all", tags=["Workout Plan Routes"], status_code=200)
async def get_all_workout_plans():
    workout_plan = WorkoutPlanController()
    return workout_plan.get_all_workout_plans()

@router.get("/active/{user_id}", tags=["Workout Plan Routes"], status_code=200)
async def get_user_active_workout_plans(user_id):
    workout_plan = WorkoutPlanController()
    return workout_plan.get_user_active_workout_plans(user_id)

@router.post("/create", tags=["Workout Plan Routes"], status_code=200)
async def create_workout_plan(payload: list[WorkoutPlan]):
    workout_plan = WorkoutPlanController()
    return workout_plan.create_workout_plan(payload)

@router.delete("/delete", tags=["Workout Plan Routes"], status_code=200)
async def delete_exercise(payload: DeleteWorkoutPlan):
    workout_plan = WorkoutPlanController()
    return workout_plan.delete_workout_plan(payload)
