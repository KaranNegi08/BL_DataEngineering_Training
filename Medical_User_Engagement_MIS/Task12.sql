-- SELECT * FROM appointments;
-- CREATE PROCEDURE insert_appointment_data(
-- p_id  INT,
-- d_id INT,
-- a_date DATE,
-- a_time TIME,
-- c_status VARCHAR(50)
-- )
-- LANGUAGE plpgsql
-- AS $$
-- BEGIN
-- INSERT INTO appointments(patient_id,doctor_id,appointment_date,appointment_time,current_status) VALUES(
-- p_id,
-- d_id ,
-- a_date ,
-- a_time ,
-- c_status 
-- );
-- END;
-- $$;

-- CALL insert_appointment_data(2,3,'2026-6-05','12:00:00','Scheduled');



-- SELECT * FROM user_engagement;
-- CREATE OR REPLACE PROCEDURE update_engagement(
-- p_id INT,
-- l_count INT,
-- s_duration INT
-- )
-- LANGUAGE plpgsql
-- AS $$
-- BEGIN
-- UPDATE user_engagement SET
-- login_count = l_count,
-- session_duration=s_duration,
-- last_login = CURRENT_TIMESTAMP
--  WHERE patient_id=p_id;
-- END;
-- $$;

-- CALL update_engagement(1,10,100);


-- SELECT * FROM user_engagement;
-- CREATE OR REPLACE PROCEDURE delete_users()
-- LANGUAGE plpgsql
-- AS $$
-- BEGIN
-- DELETE FROM user_engagement WHERE last_login < CURRENT_DATE - INTERVAL '30 days';
-- END;
-- $$;

-- CALL delete_users()
