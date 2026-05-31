-- EXPLAIN ANALYZE 
-- SELECT fname,lname FROM patients; 

-- CREATE INDEX patient_idx ON patients(fname,lname);

-- EXPLAIN ANALYZE 
-- SELECT fname,lname FROM patients; 


-- EXPLAIN ANALYZE 
-- SELECT fname,lname FROM doctors; 
-- CREATE INDEX doctor_name_idx on doctors(fname,lname);
-- EXPLAIN ANALYZE 
-- SELECT fname,lname FROM doctors; 


-- EXPLAIN ANALYZE 
-- SELECT appointment_date FROM appointments;
-- CREATE INDEX idx_appointment on appointments(appointment_date);
-- EXPLAIN ANALYZE 
-- SELECT appointment_date FROM appointments;
