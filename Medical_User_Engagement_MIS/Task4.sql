-- INSERT INTO patients (fname, lname, age, gender, email, phone, city)
-- VALUES
-- ('Aarav', 'Sharma', 25, 'Male', 'aarav.sharma@gmail.com', '9876543210', 'Delhi'),

-- ('Priya', 'Verma', 30, 'Female', 'priya.verma@gmail.com', '9876543211', 'Mumbai'),

-- ('Rohan', 'Singh', 28, 'Male', 'rohan.singh@gmail.com', '9876543212', 'Lucknow'),

-- ('Sneha', 'Gupta', 22, 'Female', 'sneha.gupta@gmail.com', '9876543213', 'Agra'),

-- ('Karan', 'Mehta', 35, 'Male', 'karan.mehta@gmail.com', '9876543214', 'Jaipur'),

-- ('Ananya', 'Joshi', 27, 'Female', 'ananya.joshi@gmail.com', '9876543215', 'Pune'),

-- ('Vikram', 'Yadav', 40, 'Male', 'vikram.yadav@gmail.com', '9876543216', 'Kanpur'),

-- ('Ishita', 'Kapoor', 24, 'Female', 'ishita.kapoor@gmail.com', '9876543217', 'Noida'),

-- ('Rahul', 'Nair', 32, 'Male', 'rahul.nair@gmail.com', '9876543218', 'Bangalore'),

-- ('Meera', 'Reddy', 29, 'Female', 'meera.reddy@gmail.com', '9876543219', 'Hyderabad'),

-- ('Aditya', 'Chauhan', 31, 'Male', 'aditya.chauhan@gmail.com', '9876543220', 'Chandigarh'),

-- ('Pooja', 'Malhotra', 26, 'Female', 'pooja.malhotra@gmail.com', '9876543221', 'Bhopal'),

-- ('Nikhil', 'Patel', 38, 'Male', 'nikhil.patel@gmail.com', '9876543222', 'Ahmedabad'),

-- ('Simran', 'Kaur', 21, 'Female', 'simran.kaur@gmail.com', '9876543223', 'Amritsar'),

-- ('Arjun', 'Das', 45, 'Male', 'arjun.das@gmail.com', '9876543224', 'Kolkata'),

-- ('Neha', 'Saxena', 33, 'Female', 'neha.saxena@gmail.com', '9876543225', 'Indore'),

-- ('Manav', 'Bansal', 37, 'Male', 'manav.bansal@gmail.com', '9876543226', 'Surat'),

-- ('Ritika', 'Agarwal', 23, 'Female', 'ritika.agarwal@gmail.com', '9876543227', 'Varanasi'),

-- ('Dev', 'Khanna', 41, 'Male', 'dev.khanna@gmail.com', '9876543228', 'Patna'),

-- ('Tanya', 'Arora', 28, 'Others', 'tanya.arora@gmail.com', '9876543229', 'Gurgaon');

-- SELECT * FROM patients;


-- INSERT INTO doctors 
-- (fname, lname, specialization, email, phone, experience_years)
-- VALUES
-- ('Rajesh', 'Sharma', 'Cardiologist', 'rajesh.sharma@gmail.com', '9123456780', 12),

-- ('Anita', 'Verma', 'Dermatologist', 'anita.verma@gmail.com', '9123456781', 8),

-- ('Suresh', 'Patel', 'Orthopedic', 'suresh.patel@gmail.com', '9123456782', 15),

-- ('Neha', 'Kapoor', 'Neurologist', 'neha.kapoor@gmail.com', '9123456783', 10),

-- ('Vikas', 'Singh', 'Pediatrician', 'vikas.singh@gmail.com', '9123456784', 7),

-- ('Pooja', 'Mehta', 'Gynecologist', 'pooja.mehta@gmail.com', '9123456785', 9),

-- ('Arun', 'Yadav', 'ENT Specialist', 'arun.yadav@gmail.com', '9123456786', 11),

-- ('Snehal', 'Joshi', 'Psychiatrist', 'snehal.joshi@gmail.com', '9123456787', 6),

-- ('Kunal', 'Malhotra', 'General Physician', 'kunal.malhotra@gmail.com', '9123456788', 14),

-- ('Ritika', 'Agarwal', 'Ophthalmologist', 'ritika.agarwal@gmail.com', '9123456789', 5);

-- SELECT * FROM doctors;

-- INSERT INTO appointments
-- (patient_id, doctor_id, appointment_date, appointment_time, status)
-- VALUES
-- (1, 1, '2026-05-01', '09:00:00', 'Scheduled'),
-- (2, 2, '2026-05-01', '10:00:00', 'Completed'),
-- (3, 3, '2026-05-02', '11:00:00', 'Scheduled'),
-- (4, 4, '2026-05-02', '12:00:00', 'Cancelled'),
-- (5, 5, '2026-05-03', '09:30:00', 'Completed'),

-- (6, 6, '2026-05-03', '10:30:00', 'Scheduled'),
-- (7, 7, '2026-05-04', '11:30:00', 'Scheduled'),
-- (8, 8, '2026-05-04', '01:00:00', 'Completed'),
-- (9, 9, '2026-05-05', '02:00:00', 'Scheduled'),
-- (10, 10, '2026-05-05', '03:00:00', 'Cancelled'),

-- (11, 1, '2026-05-06', '09:15:00', 'Completed'),
-- (12, 2, '2026-05-06', '10:15:00', 'Scheduled'),
-- (13, 3, '2026-05-07', '11:15:00', 'Scheduled'),
-- (14, 4, '2026-05-07', '12:15:00', 'Completed'),
-- (15, 5, '2026-05-08', '01:15:00', 'Cancelled'),

-- (16, 6, '2026-05-08', '02:15:00', 'Scheduled'),
-- (17, 7, '2026-05-09', '03:15:00', 'Completed'),
-- (18, 8, '2026-05-09', '04:15:00', 'Scheduled'),
-- (19, 9, '2026-05-10', '09:45:00', 'Completed'),
-- (20, 10, '2026-05-10', '10:45:00', 'Scheduled'),

-- (1, 2, '2026-05-11', '11:45:00', 'Cancelled'),
-- (2, 3, '2026-05-11', '12:45:00', 'Completed'),
-- (3, 4, '2026-05-12', '01:45:00', 'Scheduled'),
-- (4, 5, '2026-05-12', '02:45:00', 'Scheduled'),
-- (5, 6, '2026-05-13', '03:45:00', 'Completed'),

-- (6, 7, '2026-05-13', '04:45:00', 'Scheduled'),
-- (7, 8, '2026-05-14', '09:20:00', 'Cancelled'),
-- (8, 9, '2026-05-14', '10:20:00', 'Completed'),
-- (9, 10, '2026-05-15', '11:20:00', 'Scheduled'),
-- (10, 1, '2026-05-15', '12:20:00', 'Completed');

-- SELECT * FROM appointments;


-- INSERT INTO user_engagement
-- (patient_id, login_count, session_duration, last_login)
-- VALUES
-- (1, 5, 35, '2026-05-01 09:15:00'),
-- (2, 8, 50, '2026-05-01 10:20:00'),
-- (3, 3, 20, '2026-05-01 11:10:00'),
-- (4, 10, 65, '2026-05-01 12:00:00'),
-- (5, 6, 40, '2026-05-01 01:25:00'),

-- (6, 12, 75, '2026-05-02 09:40:00'),
-- (7, 4, 18, '2026-05-02 10:15:00'),
-- (8, 9, 55, '2026-05-02 11:45:00'),
-- (9, 7, 42, '2026-05-02 12:30:00'),
-- (10, 15, 90, '2026-05-02 01:10:00'),

-- (11, 2, 12, '2026-05-03 09:05:00'),
-- (12, 11, 70, '2026-05-03 10:25:00'),
-- (13, 5, 33, '2026-05-03 11:15:00'),
-- (14, 6, 38, '2026-05-03 12:45:00'),
-- (15, 14, 85, '2026-05-03 01:55:00'),

-- (16, 7, 48, '2026-05-04 09:35:00'),
-- (17, 8, 52, '2026-05-04 10:10:00'),
-- (18, 3, 25, '2026-05-04 11:05:00'),
-- (19, 9, 58, '2026-05-04 12:20:00'),
-- (20, 10, 67, '2026-05-04 01:40:00'),

-- (1, 13, 88, '2026-05-05 09:50:00'),
-- (2, 4, 22, '2026-05-05 10:35:00'),
-- (3, 6, 39, '2026-05-05 11:25:00'),
-- (4, 7, 45, '2026-05-05 12:15:00'),
-- (5, 8, 53, '2026-05-05 01:05:00'),

-- (6, 9, 60, '2026-05-06 09:45:00'),
-- (7, 5, 28, '2026-05-06 10:55:00'),
-- (8, 12, 80, '2026-05-06 11:35:00'),
-- (9, 6, 37, '2026-05-06 12:50:00'),
-- (10, 4, 21, '2026-05-06 01:30:00'),

-- (11, 15, 95, '2026-05-07 09:25:00'),
-- (12, 7, 49, '2026-05-07 10:45:00'),
-- (13, 3, 19, '2026-05-07 11:55:00'),
-- (14, 5, 31, '2026-05-07 12:05:00'),
-- (15, 9, 63, '2026-05-07 01:20:00'),

-- (16, 11, 76, '2026-05-08 09:10:00'),
-- (17, 6, 35, '2026-05-08 10:40:00'),
-- (18, 8, 57, '2026-05-08 11:30:00'),
-- (19, 13, 82, '2026-05-08 12:25:00'),
-- (20, 7, 46, '2026-05-08 01:15:00'),

-- (1, 10, 68, '2026-05-09 09:05:00'),
-- (2, 5, 29, '2026-05-09 10:50:00'),
-- (3, 14, 92, '2026-05-09 11:20:00'),
-- (4, 8, 54, '2026-05-09 12:35:00'),
-- (5, 6, 41, '2026-05-09 01:45:00'),

-- (6, 9, 61, '2026-05-10 09:55:00'),
-- (7, 4, 23, '2026-05-10 10:30:00'),
-- (8, 11, 74, '2026-05-10 11:40:00'),
-- (9, 7, 47, '2026-05-10 12:10:00'),
-- (10, 12, 83, '2026-05-10 01:50:00');

