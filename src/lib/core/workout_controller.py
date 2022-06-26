from lib.base.base_job import BaseJob
from lib.logger.struct_log import logger
from lib.models.models import WorkoutTable, UserWorkoutPlansTable, WorkoutPlanWorkoutsTable, WorkoutPlansTable
from lib.models.models import Workouts
from sqlalchemy import select, and_


class WorkoutController(BaseJob):
    def __init__(self) -> None:
        super().__init__()

    def get_user_active_workouts(self, user_id):
        query = select(WorkoutTable) \
                    .join(WorkoutPlanWorkoutsTable,
                            WorkoutPlanWorkoutsTable.workout_id == WorkoutTable.workout_id) \
                    .join(WorkoutPlansTable,
                            WorkoutPlansTable.workout_plan_id == WorkoutPlanWorkoutsTable.workout_plan_id) \
                    .join(UserWorkoutPlansTable,
                            UserWorkoutPlansTable.workout_plan_id == WorkoutPlansTable.workout_plan_id) \
                    .where(and_(UserWorkoutPlansTable.user_id == user_id,
                                   UserWorkoutPlansTable.workout_plan_is_active == True))

        with self.session_factory() as session:
            result = session.execute(query).fetchall()
            workout_list = []
            for row in result:
                dicionario = row._mapping
                workouts = Workouts.from_orm(dicionario["WorkoutTable"])
                workout_list.append(workouts)

            if not workout_list:
                logger.info(f"Workout not found, user_id{user_id}")
                workout_list = []

            return workout_list

    def get_all_workout_plans(self):
        with self.session_factory() as session:
            return session.query(WorkoutPlansTable).all()

    def get_user_active_workout_plans(self, user_id):
        query = select(WorkoutPlansTable) \
                    .join(UserWorkoutPlansTable,
                            UserWorkoutPlansTable.workout_plan_id == WorkoutPlansTable.workout_plan_id) \
                    .where(and_(
                        UserWorkoutPlansTable.user_id == user_id,
                        UserWorkoutPlansTable.workout_plan_is_active == True))

        with self.session_factory() as session:
            active_plans = session.execute(query).fetchall()

            if not active_plans:
                logger.info(f"Workout not found, user_id{user_id}")
                active_plans = []

            return active_plans