from lib.base.base_job import BaseJob
from lib.logger.struct_log import logger
from sqlalchemy import select, and_


class ExerciseController(BaseJob):
    def __init__(self) -> None:
        super().__init__()

    def get_exercises_from_workout(self):
        ...

    def get_exercise_by_muscle_group(self):
        ...