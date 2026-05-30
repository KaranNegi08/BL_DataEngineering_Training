-- CREATE VIEW active_patients AS
-- SELECT DISTINCT patient_id AS active_patients FROM appointments WHERE current_status='Scheduled';
-- SELECT * FROM active_patients;


-- CREATE VIEW appointment_summary AS 
-- SELECT d.doctor_id,CONCAT(d.fname,' ',d.lname) AS doctore_name, p.fname, p.lname, a.appointment_date,a.appointment_time FROM doctors AS d JOIN appointments AS a ON d.doctor_id= a.doctor_id
-- JOIN patients AS p ON a.patient_id=p.patient_id ORDER BY d.doctor_id;
-- SELECT * FROM appointment_summary;


-- CREATE VIEW engagement_report AS
-- SELECT p.patient_id, CONCAT(p.fname,' ',p.lname),SUM(e.login_count) AS total_login_count,SUM(e.session_duration) AS total_session_duration FROM patients AS p JOIN user_engagement AS e ON p.patient_id=e.patient_id GROUP BY p.patient_id ORDER BY p.patient_id;
-- SELECT * FROM engagement_report;
