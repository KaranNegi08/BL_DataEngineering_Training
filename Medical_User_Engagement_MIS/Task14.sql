-- SELECT * FROM engagement_summary;
-- CREATE OR REPLACE FUNCTION update_engagement()
-- RETURNS TRIGGER
-- LANGUAGE plpgsql
-- AS $$
-- BEGIN
-- 	 UPDATE engagement_summary
-- 	 SET
-- 	  total_logins = total_logins + NEW.login_count,
--         total_sessions = total_sessions + NEW.session_duration,
--         updated_at = CURRENT_TIMESTAMP
-- 	where patient_id=NEW.patient_id;
-- 	return NEW;
-- END;
-- $$;

-- CREATE TRIGGER trg_update
-- AFTER INSERT ON user_engagement
-- FOR EACH ROW
-- EXECUTE FUNCTION update_engagement();

-- INSERT INTO user_engagement(
--     patient_id,
--     login_count,
--     session_duration
-- )
-- VALUES(
--     1,
--     30,
--     100
-- );
-- SELECT * FROM user_engagement;


-- CREATE TABLE appointment_logs(
--  log_id SERIAL PRIMARY KEY,
--  appointment_id INT,
--  patient_id INT,
--  doctor_id INT,
--  appointment_date DATE ,
--  status VARCHAR(30),
--  created_at TIMESTAMP,
--  deleted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );

-- CREATE OR REPLACE FUNCTION log_deleted_appointment()
-- returns trigger
-- LANGUAGE plpgsql
-- as $$
-- begin
--      insert into appointment_logs(
--          appointment_id,
-- 		 patient_id,
-- 		 doctor_id,
-- 		 appointment_date,
-- 		 status,
-- 		 created_at
-- 	 )values(
--          OLD.appointment_id,OLD.patient_id,
-- 		 OLD.doctor_id,OLD.appointment_date,
-- 		 OLD.current_status,OLD.created_at
-- 	 );
-- 	 return OLD;
-- end;
-- $$;

-- CREATE TRIGGER trgg_log_deleted
-- BEFORE DELETE
-- ON appointments
-- FOR EACH ROW
-- EXECUTE FUNCTION log_deleted_appointment();

-- DELETE FROM appointments
-- WHERE appointment_id = 5;

-- SELECT * FROM appointments;
-- select * from appointment_logs;