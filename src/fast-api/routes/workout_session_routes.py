
from fastapi import APIRouter, Body, status, Response
from lib.models.models import WorkoutSession
from lib.core.workout_session_controller import WorkoutSessionController

router = APIRouter(
    prefix="/workout_session",
    tags=["Workout Session Routes"]
)

@router.post("/create", tags=["Workout Session Routes"], status_code=200)
async def create_workout_sessions(payload: list[WorkoutSession]):
    workout_session = WorkoutSessionController()
    return workout_session.create_workout_session(payload)

@router.delete("/delete", tags=["Workout Session Routes"], status_code=200)
async def delete_workout_session(payload: WorkoutSession):
    workout_session = WorkoutSessionController()
    return workout_session.delete_workout_session(payload)
