INSERT INTO public.users (user_id,user_name,user_lastname,user_login,user_password,created_at) VALUES ('1AGTW234', 'Eloy', 'Herrero', 'eloy', 'senha_eloy', '2022-06-08');
INSERT INTO public.users (user_id,user_name,user_lastname,user_login,user_password,created_at) VALUES ('ASD1F2FA', 'Rafael', 'Herrero', 'rafael', 'senha_rafa', '2022-05-18');

INSERT INTO public.workouts (workout_id,workout_name,description,created_at) VALUES ('WORKOUT01', 'Treino A', 'treino para realizar no primeiro dia de treino da semana', '2000-01-01');

INSERT INTO public.exercises (exercise_id,exercise_name,description,created_at) VALUES ('AGACHA_ID', 'Agachamento Livre', 'Não usar almofadinha', '2023-09-05');

INSERT INTO public.users_workouts (user_workout_id,user_id,workout_id,created_at) VALUES ('RAFA_TREINO A', 'ASD1F2FA', 'WORKOUT01', '2022-01-01', '1999-03-05');

-- INSERT INTO public.workout_periodizacao (workout_periodizacao_id ,periodizacao_name,user_id,workout_id,created_at) VALUES ();

-- INSERT INTO public.workouts_exercises (workout_exercise_id,workout_id,exercise_id,default_reps,created_at) VALUES ();

-- INSERT INTO public.workout_session (workout_session_id,user_id,workout_id,session_start,session_end,created_at) VALUES ();

-- INSERT INTO public.users_workouts_exercises (user_workout_exercise_id,user_workout_id,exercise_id,number_of_reps_executed,created_at) VALUES ();
