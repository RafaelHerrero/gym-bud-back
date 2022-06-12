
CREATE TABLE public.users (
	user_id TEXT NOT NULL,
	user_firstname text NOT NULL,
	user_lastname text NOT NULL,
	user_login TEXT NOT NULL,
	user_password TEXT NOT NULL,
	updated_at timestamp with time zone DEFAULT now(),
	created_at timestamp with time zone DEFAULT now(),
	primary key(user_id)
);

CREATE TABLE public.workouts (
    workout_id TEXT NOT NULL,
    workout_name TEXT NOT NULL,
    workout_description TEXT,
	created_at timestamp with time zone,
	updated_at timestamp with time zone DEFAULT now(),
    primary key(workout_id)
);


-- CREATE TABLE public.exercises (
--     exercise_id TEXT NOT NULL,
--     exercise_name TEXT NOT NULL,
--     exercise_description TEXT,
-- 	created_at timestamp with time zone,
-- 	updated_at timestamp with time zone DEFAULT now(),
--     primary key(exercise_id)
-- );

-- CREATE TABLE public.users_workouts (
--     user_workout_id TEXT NOT NULL,
--     user_id TEXT references public.users(user_id),
--     workout_id TEXT references public.workouts(workout_id),
-- 	created_at timestamp with time zone,
-- 	updated_at timestamp with time zone DEFAULT now(),
--     primary key(user_workout_id)
-- );

-- CREATE TABLE public.users_workout_periodizacao (
--     workout_periodizacao_id TEXT NOT NULL,
--     periodizacao_name TEXT NOT NULL,
--     user_id TEXT references public.users(user_id),
--     workout_id TEXT references public.workouts(workout_id),
-- 	created_at timestamp with time zone,
-- 	updated_at timestamp with time zone DEFAULT now(),
--     primary key(workout_periodizacao_id)
-- );

-- CREATE TABLE public.workouts_exercises (
--     workout_exercise_id TEXT NOT NULL,
--     workout_id TEXT references public.workouts(workout_id),
--     exercise_id TEXT references public.exercises(exercise_id),
--     default_reps INT,
-- 	created_at timestamp with time zone,
-- 	updated_at timestamp with time zone DEFAULT now(),
--     primary key (workout_exercise_id)
-- );

-- CREATE TABLE public.workout_session (
--     workout_session_id TEXT NOT NULL,
--     user_id TEXT references public.users(user_id),
--     workout_id TEXT references public.workouts(workout_id),
--     session_start timestamp with time zone,
--     session_end timestamp with time zone,
-- 	created_at timestamp with time zone,
-- 	updated_at timestamp with time zone DEFAULT now(),
--     primary key( workout_session_id)
-- );

-- CREATE TABLE public.users_workouts_exercises (
--     user_workout_exercise_id TEXT NOT NULL,
--     user_workout_id TEXT references public.users_workouts(user_workout_id),
--     exercise_id TEXT references public.exercises(exercise_id),
--     number_of_reps_executed INT,
-- 	created_at timestamp with time zone,
-- 	updated_at timestamp with time zone DEFAULT now(),
--     primary key(user_workout_exercise_id)
-- );
