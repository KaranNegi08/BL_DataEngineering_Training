select * from Employees;

-- INSERT INTO Employees VALUES(103,'Priya','Singh','priya.sinigh@gmail.com','HR',45000.00,'2019-03-22'),(104,'Rahul','Sharma','rahul.sharma@gmail.com','IT',65000.00,'2020-01-15'),

-- (105,'Anjali','Verma','anjali.verma@gmail.com','Finance',55000.00,'2018-07-10'),

-- (106,'Amit','Kumar','amit.kumar@gmail.com','Marketing',48000.00,'2021-05-18'),

-- (107,'Sneha','Gupta','sneha.gupta@gmail.com','HR',47000.00,'2019-11-25'),

-- (108,'Vikas','Mehta','vikas.mehta@gmail.com','IT',72000.00,'2017-09-30'),

-- (109,'Neha','Joshi','neha.joshi@gmail.com','Sales',50000.00,'2022-02-14'),

-- (110,'Arjun','Patel','arjun.patel@gmail.com','Operations',58000.00,'2020-08-05');

-- SELECT * FROM Employees where dept='HR' and salary > 45000;
-- SELECT * FROM Employees WHERE dept IN ('HR','Finance');
-- SELECT * FROM Employees ORDER BY salary DESC;
-- SELECT * FROM Employees WHERE salary BETWEEN 40000 AND 55000;
-- SELECT DISTINCT dept from Employees ;
-- SELECT * from Employees ORDER BY emp_id DESC LIMIT 3;

-- SELECT fname from Employees WHERE fname LIKE '%n%';
-- SELECT dept from Employees WHERE dept like '___%';

-- SELECT dept , COUNT(*) from Employees GROUP BY dept;
-- SELECT dept , AVG(salary) FROM Employees GROUP BY dept HAVING AVG(salary) > 50000;

-- SELECT  COUNT(*) as total_employees from Employees
-- SELECT MAX(salary) FROM Employees;
-- SELECT SUM(salary) FROM Employees;






