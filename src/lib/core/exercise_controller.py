from lib.base.base_job import BaseJob
from lib.logger.struct_log import logger
from sqlalchemy import select, and_

from lib.models.models import (
    ExercisesTable, WorkoutPlanWorkoutsTable,
    WorkoutsTable, WorkoutExercisesTable, WorkoutPlansTable,
    UserWorkoutPlansTable)


class ExerciseController(BaseJob):
    def __init__(self) -> None:
        super().__init__()

    def get_exercises_from_workout(self, user_id: str, workout_id: str):
        query = select(ExercisesTable, WorkoutExercisesTable) \
                    .join(WorkoutExercisesTable,
                            WorkoutExercisesTable.exercise_id == ExercisesTable.exercise_id) \
                    .join(WorkoutsTable,
                            WorkoutsTable.workout_id == WorkoutExercisesTable.workout_id) \
                    .join(WorkoutPlanWorkoutsTable,
                            WorkoutPlanWorkoutsTable.workout_id == WorkoutsTable.workout_id) \
                    .join(WorkoutPlansTable,
                            WorkoutPlansTable.workout_plan_id == WorkoutPlanWorkoutsTable.workout_plan_id) \
                    .join(UserWorkoutPlansTable,
                            UserWorkoutPlansTable.workout_plan_id == WorkoutPlansTable.workout_plan_id) \
                    .where(and_(UserWorkoutPlansTable.user_id == user_id,
                                WorkoutsTable.workout_id == workout_id))

        with self.session_factory() as session:
            result = session.execute(query).fetchall()
            exercise_list = []
            for row in result:
                dicionario = row._mapping
                print(dicionario)
                exercise_list.append(dicionario)

            if not exercise_list:
                logger.info(f"Exercise not found, user_id{user_id}")
                exercise_list = []

            return exercise_list


    def get_exercise_by_muscle_group(self):
        ...