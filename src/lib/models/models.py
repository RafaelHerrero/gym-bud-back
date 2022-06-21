from sqlalchemy import Column, String, DateTime, ForeignKey, Boolean
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


class WorkoutTable(Base):
    __tablename__ = 'workouts'

    workout_id = Column(String, primary_key=True)
    workout_name = Column(String)
    workout_description = Column(String)
    updated_at = Column(DateTime)
    created_at = Column(DateTime)


class WorkoutPlansTable(Base):
    __tablename__ = 'workout_plans'

    workout_plan_id = Column(String, primary_key=True)
    workout_plan_name = Column(String)
    workout_plan_description = Column(String)
    updated_at = Column(DateTime)
    created_at = Column(DateTime)


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

    workout = relationship("WorkoutTable")
    exercise_plan = relationship("WorkoutPlansTable")



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
