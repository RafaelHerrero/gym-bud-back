from fastapi import HTTPException, status
from lib.base.base_job import BaseJob
from lib.logger.struct_log import logger
from lib.models.models import WorkoutSession, WorkoutSessionTable
from sqlalchemy import select, and_


class WorkoutSessionController(BaseJob):
    def __init__(self) -> None:
        super().__init__()

    def create_workout_session(self, payload: list[WorkoutSession]):
        workout_session_instance = [WorkoutSessionTable(**row.dict()) for row in payload]
        ids = [row.workout_session_id for row in payload]
        with self.session_factory() as session:
            query = select(WorkoutSessionTable).where(WorkoutSessionTable.workout_session_id.in_(ids))
            existing_workout_session: list[WorkoutSession] = session.execute(query).fetchall()

            if not existing_workout_session:
                session.add_all(workout_session_instance)
                session.commit()
            else:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="Workout Session Already Exists"
                )

    def delete_workout_session(self, payload: WorkoutSession):
        with self.session_factory() as session:
            query = select(WorkoutSessionTable).where(
                WorkoutSessionTable.workout_session_id == payload.workout_session_id
            )
            existing_workout_session: list[WorkoutSession] = session.execute(query).fetchall()

            if existing_workout_session:
                session.delete(existing_workout_session[0])
                session.commit()
            else:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Workout Session Not Found"
                )
