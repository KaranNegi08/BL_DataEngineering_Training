-- SELECT p.patient_id, CONCAT(p.fname,' ',p.lname) AS full_name, e.login_count FROM patients AS p JOIN user_engagement AS e ON p.patient_id = e.patient_id WHERE e.login_count = (
-- SELECT MAX(login_count) FROM user_engagement
-- );

-- SELECT d.doctor_id , d.fname, d.lname, COUNT(a.appointment_id) AS total_appointments FROM doctors AS d  JOIN appointments AS a ON d.doctor_id = a.doctor_id GROUP BY d.doctor_id , d.fname, d.lname HAVING COUNT(a.appointment_id) = (
-- SELECT MAX(appointment_count) FROM (
-- 	SELECT COUNT(*) AS appointment_count FROM appointments GROUP BY doctor_id
-- ) 
-- );

-- SELECT p.patient_id, CONCAT(p.fname, ' ',p.lname), e.session_duration FROM patients AS p JOIN user_engagement AS e ON p.patient_id = e.patient_id WHERE e.session_duration > (
-- SELECT AVG(session_duration) FROM user_engagement
-- )
