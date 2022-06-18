from fastapi import Response, status
from lib.base.base_job import BaseJob
from lib.errors.errors import WorkoutNotFoundError
from lib.models.models import WorkoutTable, UserWorkoutPlansTable, WorkoutPlanWorkoutsTable


class WorkoutService(BaseJob):
    def __init__(self) -> None:
        super().__init__()

    def get_user_active_workout(self, user_id):
        with self.session_factory() as session:
            active_plan = session.query(WorkoutPlanWorkoutsTable) \
                .join(UserWorkoutPlansTable, UserWorkoutPlansTable.user_id == user_id) \
                .join(WorkoutTable) \
                .filter(UserWorkoutPlansTable.exercise_plan_is_active == True) \
                .all()

            if not active_plan:
                raise WorkoutNotFoundError(user_id)

            return active_plan
