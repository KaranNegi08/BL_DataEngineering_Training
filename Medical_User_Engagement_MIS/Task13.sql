-- CREATE OR REPLACE FUNCTION total_login(p_id INT)
-- RETURNS INT
-- LANGUAGE plpgsql
-- AS $$
-- BEGIN
-- RETURN (SELECT SUM(login_count) AS logins FROM user_engagement WHERE patient_id=p_id  );
-- END;
-- $$;


-- DROP FUNCTION total_login;
-- SELECT * FROM total_login(1);

-- SELECT * FROM appointments;
-- CREATE OR REPLACE FUNCTION count_appointment(d_id INT)
-- RETURNS INT
-- LANGUAGE plpgsql
-- AS $$
-- BEGIN
-- RETURN(
-- SELECT COUNT(*) FROM appointments WHERE doctor_id=d_id
-- );
-- END;
-- $$;

-- SELECT * FROM count_appointment(1);

-- SELECT * FROM user_engagement;
-- CREATE OR REPLACE FUNCTION avg_duration()
-- RETURNS INT
-- LANGUAGE plpgsql
-- AS $$
-- BEGIN
-- RETURN(
-- SELECT AVG(session_duration) FROM user_engagement
-- );
-- END;
-- $$;

-- SELECT * FROM avg_duration();
