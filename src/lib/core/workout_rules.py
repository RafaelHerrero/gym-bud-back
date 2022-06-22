from fastapi import Response, status
from lib.base.base_job import BaseJob
from lib.errors.errors import WorkoutNotFoundError
from lib.logger.struct_log import logger
from lib.models.models import WorkoutTable, UserWorkoutPlansTable, WorkoutPlanWorkoutsTable, WorkoutPlansTable


class WorkoutService(BaseJob):
    def __init__(self) -> None:
        super().__init__()

    def get_user_active_workout(self, user_id):
        with self.session_factory() as session:
            active_plan = session.query(WorkoutTable) \
                .join(UserWorkoutPlansTable, UserWorkoutPlansTable.user_id == user_id) \
                .join(WorkoutPlanWorkoutsTable) \
                .filter(UserWorkoutPlansTable.workout_plan_is_active == True) \
                .all()

            if not active_plan:
                logger.info(f"Workout not found, user_id{user_id}")
                active_plan = []
                # raise WorkoutNotFoundError(user_id)

            return active_plan

    def get_all_workout_plans(self):
        print("a")
        with self.session_factory() as session:
            return session.query(WorkoutPlansTable).all()
