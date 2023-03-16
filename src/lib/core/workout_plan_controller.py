from lib.base.base_job import BaseJob
from lib.logger.struct_log import logger
from lib.models.models import UserWorkoutPlansTable, WorkoutPlansTable, WorkoutPlan, DeleteWorkoutPlan
from sqlalchemy import select, and_
from fastapi import status, HTTPException


class WorkoutPlanController(BaseJob):
    def __init__(self) -> None:
        super().__init__()

    def get_all_workout_plans(self):
        with self.session_factory() as session:
            return session.query(WorkoutPlansTable).all()

    def get_user_active_workout_plans(self, user_id) -> list:
        query = select(WorkoutPlansTable) \
                    .join(UserWorkoutPlansTable,
                            UserWorkoutPlansTable.workout_plan_id == WorkoutPlansTable.workout_plan_id) \
                    .where(and_(
                        UserWorkoutPlansTable.user_id == user_id,
                        UserWorkoutPlansTable.workout_plan_is_active == True))

        with self.session_factory() as session:
            active_workout_plans = session.execute(query).fetchall()
            workout_plan_list = []
            for row in active_workout_plans:
                dicionario = row._mapping
                workouts = WorkoutPlan.from_orm(dicionario["WorkoutPlansTable"])
                workout_plan_list.append(workouts)

            if not workout_plan_list:
                logger.info(f"Workout Plans not found, user_id{user_id}")
                workout_plan_list = []

            return workout_plan_list

    def create_workout_plan(self, payload: list[WorkoutPlan]):
        with self.session_factory() as session:
            ids = [row.workout_plan_id for row in payload]
            insert_values = [WorkoutPlansTable(**row.dict()) for row in payload]
            query = select(WorkoutPlansTable).where(WorkoutPlansTable.workout_plan_id.in_(ids))
            result = session.execute(query).fetchall()

            if not result:
                session.add_all(insert_values)
                session.commit()
            else:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="Workout Plan Already Exists"
                )
            return True

    def delete_workout_plan(self, payload: DeleteWorkoutPlan):
        with self.session_factory() as session:
            query = select(WorkoutPlansTable).where(WorkoutPlansTable.workout_plan_id == payload.workout_plan_id)
            result = session.execute(query).fetchall()
            if not result:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Workout Plan Not Found"
                )
            else:
                session.query(WorkoutPlansTable).filter(WorkoutPlansTable.workout_plan_id == payload.workout_plan_id).delete()
                session.commit()
                return True