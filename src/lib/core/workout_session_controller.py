from fastapi import HTTPException, status
from lib.base.base_job import BaseJob
from lib.logger.struct_log import logger
from lib.models.models import WorkoutSession, WorkoutSessionTable
from sqlalchemy import select, and_


class WorkoutSessionController(BaseJob):
    def __init__(self) -> None:
        super().__init__()

    def create_workout_session(self, payload: WorkoutSession):
        workout_session_instance = WorkoutSessionTable(**payload.dict())
        with self.session_factory() as session:
            entity: WorkoutSession = session.query(WorkoutSessionTable).filter(
                WorkoutSessionTable.workout_session_id == payload.workout_session_id).first()

            if not entity:
                session.add(workout_session_instance)
                session.commit()
            else:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="Workout Session Already Exists"
                )
