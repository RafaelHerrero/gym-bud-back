INSERT INTO public.users (user_id,user_firstname,user_lastname,user_login,user_password,created_at) VALUES ('1AGTW234', 'Eloy', 'Herrero', 'eloy', 'senha_eloy', '2022-06-08');
INSERT INTO public.users (user_id,user_firstname,user_lastname,user_login,user_password,created_at) VALUES ('ASD1F2FA', 'Rafael', 'Herrero', 'rafael', 'senha_rafa', '2022-05-18');
INSERT INTO public.users (user_id,user_firstname,user_lastname,user_login,user_password,created_at) VALUES ('BKSUFHE3', 'Thales', 'Fernandes', 'thales', 'senha_thales', '2022-06-11');

-- INSERT INTO public.workouts (workout_id,workout_name,workout_description,created_at) VALUES ('WORKOUT01', 'Treino A', 'treino para realizar no primeiro dia de treino da semana', '2000-01-01');

-- INSERT INTO public.exercises (exercise_id,exercise_name,exercise_description,created_at) VALUES ('AGACHA_ID', 'Agachamento Livre', 'Não usar almofadinha', '2023-09-05');
-- INSERT INTO public.exercises (exercise_id,exercise_name,exercise_description,created_at) VALUES ('SUPINO_ID', 'Supino', 'Supino de segunda', '2022-06-11');
-- INSERT INTO public.exercises (exercise_id,exercise_name,exercise_description,created_at) VALUES ('REMADA_ID', 'Remada Curvada', 'Não usar o remo', '2022-06-11');

-- INSERT INTO public.users_workouts (user_workout_id,user_id,workout_id,created_at) VALUES ('RAFA_TREINO A', 'ASD1F2FA', 'WORKOUT01', '2022-01-01', '1999-03-05');

-- INSERT INTO public.users_workout_periodizacao (workout_periodizacao_id ,periodizacao_id,user_id,workout_id,created_at) VALUES ('RAFA_FORCA_TREINO A', 'Forca', 'ASD1F2FA', 'WORKOUT01', '2022-06-11');

-- INSERT INTO periodizacao (periodizacao_id, periodizacao_name, created_at) VALUES ()

-- INSERT INTO public.workouts_exercises (workout_exercise_id,workout_id,exercise_id,default_reps,created_at) VALUES ('WORKOUT01_AGACHA', 'WORKOUT01', 'AGACHA_ID', 10, '2022-06-10' );
-- INSERT INTO public.workouts_exercises (workout_exercise_id,workout_id,exercise_id,default_reps,created_at) VALUES ('WORKOUT01_SUPINO', 'WORKOUT01', 'SUPINO_ID', 12, '2022-06-10' );
-- INSERT INTO public.workouts_exercises (workout_exercise_id,workout_id,exercise_id,default_reps,created_at) VALUES ('WORKOUT01_REMADA', 'WORKOUT01', 'REMADA_ID', 15, '2022-06-10' );

-- INSERT INTO public.workouts_exercises_series (workout_exercise_series_id, workout_id, exercise_id, series_id, series_number, created_at) VALUES ('WORKOUT01_TREINOO A', 'WORKOUT01', 'AGACHA_ID', 'SERIES3', 3, '2022-05-01');
-- INSERT INTO public.workouts_exercises_series (workout_exercise_series_id, workout_id, exercise_id, series_id, series_number, created_at) VALUES ('WORKOUT01_TREINOO A', 'WORKOUT01', 'AGACHA_ID', 'SERIES3', 3, '2022-05-01');

-- INSERT INTO public.workouts_exercises_reps (workout_exercise_reps_id, workoiut_id, exercide_id, reps_id, reps_number, created_at) VALES ();

-- INSERT INTO public.workouts_exercides_desc (workout_exercise_desc_id, workout_id, exercise_id, desc_id, description_field, created_at) VALUES ();

-- INSERT INTO public.seres (series_id, series_number, created_at) VALUES ();

-- INSERT INTO public.reps (reps_id, reps_number, created_at) VALUES ();

-- INSERT INTO public.exercise_description (description_id, description_name, description_filed, created_at) VALUES ();




-- INSERT INTO public.workout_session (workout_session_id,user_id,workout_id,session_start,session_end,created_at) VALUES ();

-- INSERT INTO public.users_workouts_exercises (user_workout_exercise_id,user_workout_id,exercise_id,number_of_reps_executed,created_at) VALUES ();


-- -> SUPINO 3 SÉRIES DE 10 REPETIÇÕES
-- -> AGACHAMENDO 1 SÉRIE DE TIPO_DE_SERIE (LOADING_SET (3 SÉRIES DE 8 REP))

-- FORCA 