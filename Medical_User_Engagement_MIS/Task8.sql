-- SELECT CONCAT(p.fname, ' ',p.lname) AS patient_name , CONCAT(d.fname,' ',d.lname) AS doctor_name FROM appointments AS a JOIN patients as p ON a.patient_id = p.patient_id
-- JOIN doctors AS d ON a.doctor_id = d.doctor_id;

-- SELECT p.patient_id, CONCAT(p.fname,' ',p.lname) AS patient_name FROM patients AS p LEFT JOIN appointments AS a ON p.patient_id = a.patient_id WHERE a.patient_id IS NULL; 
