
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

CREATE TABLE public.exercise_plans (
    exercise_plan_id TEXT UNIQUE NOT NULL,
    exercise_plan_name TEXT NOT NULL,
    exercise_plan_description TEXT,
	created_at timestamp with time zone DEFAULT now(),
	updated_at timestamp with time zone DEFAULT now(),
    primary key(exercise_plan_id)
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


CREATE TABLE public.user_exercise_plans (
    user_exercise_plan_id TEXT UNIQUE NOT NULL,
    user_id TEXT REFERENCES public.users(user_id) NOT NULL,
    exercise_plan_id TEXT REFERENCES public.exercise_plans(exercise_plan_id) NOT NULL,
	exercise_plan_is_active BOOLEAN NOT NULL,
	exercise_plan_started_at timestamp with time zone,
	exercise_plan_finished_at timestamp with time zone,
	exercise_plan_expected_duration TEXT,
	created_at timestamp with time zone DEFAULT now(),
	updated_at timestamp with time zone DEFAULT now(),
    primary key(user_exercise_plan_id)
);

CREATE TABLE public.exercise_plan_workouts (
    exercise_plan_workout_id TEXT UNIQUE NOT NULL,
    workout_id TEXT references public.workouts(workout_id),
	exercise_plan_id TEXT references public.exercise_plans(exercise_plan_id),
	created_at timestamp with time zone,
	updated_at timestamp with time zone DEFAULT now(),
    primary key(exercise_plan_workout_id)
);

CREATE TABLE public.workout_exercises (
    workout_exercise_id TEXT UNIQUE NOT NULL,
    workout_id TEXT references public.workouts(workout_id),
    exercise_id TEXT references public.exercises(exercise_id),
	exercise_sets TEXT,
    exercise_reps TEXT,
	exercise_description TEXT,
	created_at timestamp with time zone,
	updated_at timestamp with time zone DEFAULT now(),
    primary key (workout_exercise_id)
);

CREATE TABLE public.workout_session (
    workout_session_id TEXT NOT NULL,
    user_exercise_plan_id TEXT references public.user_exercise_plans(user_exercise_plan_id),
    exercise_plan_workout_id TEXT references public.exercise_plan_workouts(exercise_plan_workout_id),
	workout_exercise_id TEXT references public.workout_exercises(workout_exercise_id),
	workout_session_sets TEXT,
	workout_session_reps TEXT,
	created_at timestamp with time zone,
	updated_at timestamp with time zone DEFAULT now(),
    primary key( workout_session_id)
);

