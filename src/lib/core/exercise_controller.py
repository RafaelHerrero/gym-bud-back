from lib.base.base_job import BaseJob
from lib.logger.struct_log import logger
from fastapi import HTTPException, status
from sqlalchemy import select, and_, inspect

from lib.models.models import (
    DeleteExercise, ExercisesTable, WorkoutPlanWorkoutsTable,
    WorkoutsTable, WorkoutExercisesTable, WorkoutPlansTable,
    UserWorkoutPlansTable, UserWorkoutExercises, Exercises)


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
            exercise_list = [dict(t) for t in result]
            result_list = []
            for row in exercise_list:
                exer_table = self.object_as_dict(row["ExercisesTable"])
                work_exer_table = self.object_as_dict(row["WorkoutExercisesTable"])
                table = UserWorkoutExercises(
                    workout_id = work_exer_table["workout_id"],
                    exercise_id = work_exer_table["exercise_id"],
                    exercise_name = exer_table["exercise_name"],
                    exercise_muscle_group = exer_table["exercise_muscle_group"],
                    exercise_reps = work_exer_table["exercise_reps"],
                    exercise_sets = work_exer_table["exercise_sets"],
                    exercise_description = exer_table["exercise_description"])
                result_list.append(table)

            return result_list


    def get_exercise_by_muscle_group(self, muscle_group: str):
        query = select(ExercisesTable).where(ExercisesTable.exercise_muscle_group == muscle_group)
        with self.session_factory() as session:
            result = session.execute(query).fetchall()
            exercise_list = [dict(t) for t in result]
            result_list = []
            for row in exercise_list:
                exer_table = self.object_as_dict(row["ExercisesTable"])
                table = Exercises(
                    exercise_id = exer_table["exercise_id"],
                    exercise_name = exer_table["exercise_name"],
                    exercise_muscle_group = exer_table["exercise_muscle_group"],
                    exercise_description = exer_table["exercise_description"])
                result_list.append(table)

            return result_list

    def object_as_dict(self, obj):
        return {c.key: getattr(obj, c.key)
                for c in inspect(obj).mapper.column_attrs}

    def create_new_exercise(self, exercise: Exercises):
        check_query = select(ExercisesTable).where(ExercisesTable.exercise_name == exercise.exercise_name)
        exercise_json = exercise.dict()
        exercise_instance = ExercisesTable(**exercise_json)

        with self.session_factory() as session:
            existing_exercise = session.execute(check_query).first()
            if not existing_exercise:
                session.add(exercise_instance)
                session.commit()
                session.refresh(exercise_instance)
                return True
            else:
                raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Exercise already exists")

    def delete_exercise(self, exercise: DeleteExercise):
        with self.session_factory() as session:
            entity: Exercises = session.query(ExercisesTable).filter(
                ExercisesTable.exercise_id == exercise.exercise_id).first()
            if not entity:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Exercise not found to be deleted"
                )
            else:
                session.delete(entity)
                session.commit()
            return True
