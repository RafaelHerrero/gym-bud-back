from datetime import datetime
from typing import Optional
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from pydantic import BaseModel

Base = declarative_base()

class UserTable(Base):
    __tablename__ = 'users'

    user_id = Column(String)
    user_firstname = Column(String)
    user_lastname = Column(String)
    user_login = Column(String, primary_key=True)
    user_password = Column(String)
    updated_at = Column(DateTime)
    created_at = Column(DateTime)


class ExercisesTable(Base):
    __tablename__ = 'exercises'

    exercise_id = Column(String, primary_key=True)
    exercise_name = Column(String)
    exercise_muscle_group = Column(String)
    exercise_description = Column(String)
    updated_at = Column(DateTime)
    created_at = Column(DateTime)

class Exercises(BaseModel):
    exercise_id: str
    exercise_name: str
    exercise_muscle_group: str
    exercise_description: str

class DeleteExercise(BaseModel):
    exercise_id: str

class WorkoutsTable(Base):
    __tablename__ = 'workouts'

    workout_id = Column(String, primary_key=True)
    workout_name = Column(String)
    workout_description = Column(String)
    updated_at = Column(DateTime)
    created_at = Column(DateTime)

class Workouts(BaseModel):
    workout_id: Optional[str]
    workout_name: Optional[str]
    workout_description: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

class DeleteWorkout(BaseModel):
    workout_id: str

class WorkoutPlansTable(Base):
    __tablename__ = 'workout_plans'

    workout_plan_id = Column(String, primary_key=True)
    workout_plan_name = Column(String)
    workout_plan_description = Column(String)
    updated_at = Column(DateTime)
    created_at = Column(DateTime)

class WorkoutPlan(BaseModel):
    workout_plan_id: Optional[str]
    workout_plan_name: Optional[str]
    workout_plan_description: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

class DeleteWorkoutPlan(BaseModel):
    workout_plan_id: str

class UserWorkoutPlansTable(Base):
    __tablename__ = 'user_workout_plans'

    user_workout_plan_id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.user_id"))
    workout_plan_id = Column(String, ForeignKey("workout_plans.workout_plan_id"))
    workout_plan_is_active = Column(Boolean)
    workout_plan_started_at = Column(DateTime)
    workout_plan_finished_at = Column(DateTime)
    workout_plan_expected_duration = Column(String)
    updated_at = Column(DateTime)
    created_at = Column(DateTime)

    user = relationship("UserTable")
    exercise_plan = relationship("WorkoutPlansTable")


class WorkoutPlanWorkoutsTable(Base):
    __tablename__ = 'workout_plan_workouts'

    workout_plan_workout_id = Column(String, primary_key=True)
    workout_id = Column(String, ForeignKey("workouts.workout_id"))
    workout_plan_id = Column(String, ForeignKey("workout_plans.workout_plan_id"))
    updated_at = Column(DateTime)
    created_at = Column(DateTime)

    workout = relationship("WorkoutsTable")
    exercise_plan = relationship("WorkoutPlansTable")

class WorkoutExercisesTable(Base):
    __tablename__ = 'workout_exercises'

    workout_exercise_id = Column(String, primary_key=True)
    workout_id = Column(String, ForeignKey("workouts.workout_id"))
    exercise_id = Column(String, ForeignKey("exercises.exercise_id"))
    exercise_reps = Column(Integer)
    exercise_sets = Column(Integer)
    exercise_description = Column(String)
    updated_at = Column(DateTime)
    created_at = Column(DateTime)

    workout = relationship("WorkoutsTable")
    exercise = relationship("ExercisesTable")

class WorkoutSessionTable(Base):
    __tablename__ = 'workout_session'

    workout_session_id = Column(String, primary_key=True)
    workout_session = Column(String)
    user_workout_plan_id = Column(String, ForeignKey("user_workout_plans.user_workout_plan_id"))
    workout_plan_workout_id = Column(String, ForeignKey("workout_plan_workouts.workout_plan_workout_id"))
    workout_exercise_id = Column(String, ForeignKey("workout_exercises.workout_exercise_id"))
    workout_session_set_number = Column(Integer)
    workout_session_reps = Column(Integer)
    workout_session_weight = Column(Integer)
    updated_at = Column(DateTime)
    created_at = Column(DateTime)

class WorkoutSession(BaseModel):
    workout_session_id: str
    workout_session: str
    user_workout_plan_id: str
    workout_plan_workout_id: str
    workout_exercise_id: str
    workout_session_set_number: int
    workout_session_reps: int
    workout_session_weight: int
    updated_at: datetime
    created_at: datetime

class CreateUser(BaseModel):
    user_firstname: str
    user_lastname: str
    user_login: str
    user_password: str

class UserId(BaseModel):
    user_id: str

class LoginUser(BaseModel):
    user_login: str
    user_password: str

class UserWorkoutExercises(BaseModel):
    workout_id: str
    exercise_id: str
    exercise_name: str
    exercise_muscle_group: str
    exercise_reps: str
    exercise_sets: str
    exercise_description: str
