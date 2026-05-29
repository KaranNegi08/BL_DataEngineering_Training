-- CREATE TABLE patients(
-- 	patient_id SERIAL PRIMARY KEY,
-- 	fname VARCHAR(50) NOT NULL,
-- 	lname VARCHAR(50) NOT NULL,
-- 	age INT CHECK (age > 0),
-- 	gender VARCHAR(20) CHECK (gender IN ('Male', 'Female','Others')),
-- 	email VARCHAR(100) UNIQUE,
-- 	phone VARCHAR(15) CHECK(LENGTH(phone)=10),
-- 	city VARCHAR(50) NOT NULL,
-- 	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- )

-- CREATE TABLE doctors(
-- 	doctor_id SERIAL PRIMARY KEY,
-- 	fname VARCHAR(50) NOT NULL,
-- 	lname VARCHAR(50) NOT NULL,
-- 	specialization VARCHAR(100) NOT NULL,
-- 	email VARCHAR(100) UNIQUE NOT NULL,
-- 	phone VARCHAR(10) CHECK (LENGTH(phone) = 10),
-- 	experience_years INT CHECK (experience_years > 0),
-- 	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP	
-- );

-- CREATE TABLE appointments(
-- 	appointment_id SERIAL PRIMARY KEY,
-- 	patient_id INT NOT NULL,
-- 	doctor_id INT NOT NULL,
-- 	appointment_date DATE NOT NULL,
-- 	appointment_time TIME NOT NULL,
-- 	status VARCHAR(50) DEFAULT 'Scheduled',
-- 	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
-- 	FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
-- 	FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
-- );

-- CREATE TABLE prescriptions(
-- 	prescription_id SERIAL PRIMARY KEY,
-- 	appointment_id INT NOT NULL,
-- 	patient_id INT NOT NULL,
-- 	doctor_id INT NOT NULL,
-- 	medicine_name VARCHAR(200) NOT NULL,
-- 	dosage VARCHAR(100) NOT NULL,
-- 	prescribed_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
-- 	FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id),
-- 	FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
-- 	FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
-- );

-- CREATE TABLE user_engagement(
-- 	engagement_id SERIAL PRIMARY KEY,
-- 	patient_id INT NOT NULL,
-- 	login_count INT DEFAULT 0,
-- 	session_duration INT CHECK (session_duration >= 0),
-- 	last_login TIMESTAMP,
-- 	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
-- 	FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
-- );


-- CREATE TABLE engagement_summary(
-- summary_id SERIAL PRIMARY KEY,
-- patient_id INT UNIQUE NOT NULL,
-- total_logins INT DEFAULT 0,
-- total_sessions INT DEFAULT 0,
-- updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
-- FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
-- );

-- CREATE TABLE medical_reports(
-- report_id SERIAL PRIMARY KEY,
-- patient_id INT NOT NULL,
-- doctor_id INT NOT NULL,
-- appointment_id INT NOT NULL,
-- report_type VARCHAR(100) NOT NULL,
-- created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
-- FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
-- FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id),
-- FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id)
-- );

