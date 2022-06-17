from fastapi import Response, status
from lib.base.base_job import BaseJob
from lib.errors.errors import UserNotFoundError, PasswordNotFoundError
from lib.models.models import WorkoutTable, UserExercisePlansTable


class WorkoutService(BaseJob):
    def __init__(self) -> None:
        super().__init__()
        self.workout_table = WorkoutTable
        self.user_exercise_plans = UserExercisePlansTable

    def get_user_active_workout(self, user_id):
        with self.session_factory() as session:
            active_plan = session.query(
                self.user_exercise_plans, self.workout_table).filter(
                    self.user_exercise_plans.user_id == user_id,
                        self.user_exercise_plans.exercise_plan_is_active == True).all()
            if not active_plan:
                raise UserNotFoundError(user_id)

            return active_plan
