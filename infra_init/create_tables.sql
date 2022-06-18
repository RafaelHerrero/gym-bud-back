
CREATE TABLE public.users (
	user_id TEXT UNIQUE NOT NULL,
	user_firstname text NOT NULL,
	user_lastname text NOT NULL,
	user_login TEXT NOT NULL,
	user_password TEXT NOT NULL,
	user_is_active BOOLEAN NOT NULL DEFAULT TRUE,
	updated_at timestamp with time zone DEFAULT now(),
	created_at timestamp with time zone DEFAULT now(),
	primary key(user_login)
);

CREATE TABLE public.workout_plans (
    workout_plan_id TEXT UNIQUE NOT NULL,
    workout_plan_name TEXT NOT NULL,
    workout_plan_description TEXT,
	created_at timestamp with time zone DEFAULT now(),
	updated_at timestamp with time zone DEFAULT now(),
    primary key(workout_plan_id)
);

CREATE TABLE public.workouts (
    workout_id TEXT UNIQUE NOT NULL,
    workout_name TEXT NOT NULL,
    workout_description TEXT,
	created_at timestamp with time zone DEFAULT now(),
	updated_at timestamp with time zone DEFAULT now(),
    primary key(workout_id)
);

CREATE TABLE public.exercises (
    exercise_id TEXT UNIQUE NOT NULL,
    exercise_name TEXT NOT NULL,
	exercise_muscle_group TEXT,
    exercise_description TEXT,
	created_at timestamp with time zone DEFAULT now(),
	updated_at timestamp with time zone DEFAULT now(),
    primary key(exercise_id)
);


CREATE TABLE public.user_workout_plans (
    user_workout_plan_id TEXT UNIQUE NOT NULL,
    user_id TEXT REFERENCES public.users(user_id) NOT NULL,
    workout_plan_id TEXT REFERENCES public.workout_plans(workout_plan_id) NOT NULL,
	workout_plan_is_active BOOLEAN NOT NULL,
	workout_plan_started_at timestamp with time zone,
	workout_plan_finished_at timestamp with time zone,
	workout_plan_expected_duration TEXT,
	created_at timestamp with time zone DEFAULT now(),
	updated_at timestamp with time zone DEFAULT now(),
    primary key(user_workout_plan_id)
);

CREATE TABLE public.workout_plan_workouts (
    workout_plan_workout_id TEXT UNIQUE NOT NULL,
    workout_id TEXT references public.workouts(workout_id),
	workout_plan_id TEXT references public.workout_plans(workout_plan_id),
	created_at timestamp with time zone DEFAULT now(),
	updated_at timestamp with time zone DEFAULT now(),
    primary key(workout_plan_workout_id)
);

CREATE TABLE public.workout_exercises (
    workout_exercise_id TEXT UNIQUE NOT NULL,
    workout_id TEXT references public.workouts(workout_id),
    exercise_id TEXT references public.exercises(exercise_id),
	exercise_sets TEXT,
    exercise_reps TEXT,
	exercise_description TEXT,
	created_at timestamp with time zone DEFAULT now(),
	updated_at timestamp with time zone DEFAULT now(),
    primary key (workout_exercise_id)
);

CREATE TABLE public.workout_session (
    workout_session_id TEXT NOT NULL,
    user_workout_plan_id TEXT references public.user_workout_plans(user_workout_plan_id),
    workout_plan_workout_id TEXT references public.workout_plan_workouts(workout_plan_workout_id),
	workout_exercise_id TEXT references public.workout_exercises(workout_exercise_id),
	workout_session_sets TEXT,
	workout_session_reps TEXT,
	created_at timestamp with time zone DEFAULT now(),
	updated_at timestamp with time zone DEFAULT now(),
    primary key( workout_session_id)
);

