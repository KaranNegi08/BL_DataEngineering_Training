-- TASK1 --
-- SELECT CONCAT_WS(':',emp_id,fname,lname) FROM Employees;

-- TASK2
-- SELECT CONCAT_WS(':',emp_id,CONCAT(fname, ' ',lname),dept,salary) FROM Employees;

-- TASK3
-- SELECT CONCAT_WS(':',emp_id,fname,UPPER(dept)) FROM Employees;

-- TASK4
-- SELECT CONCAT(LEFT(dept,1),emp_id, ' ',fname) FROM Employees;

-- TASK5
-- SELECT DISTINCT dept FROM Employees;

-- TASK6
-- SELECT * FROM Employees ORDER BY salary DESC;

-- TASK7
-- SELECT * FROM Employees LIMIT 3;

-- TASK8
-- SELECT * FROM EmployeeS WHERE fname LIKE 'A%'; 

-- TASK9
-- SELECT * FROM Employees WHERE LENGTH(lname)=5;

-- TASK10
-- SELECT COUNT(emp_id) FROM Employees;

-- TASK11
-- SELECT dept, COUNT(*) FROM Employees GROUP BY dept;

-- TASK12
-- SELECT MIN(salary) FROM Employees;

-- TASK13
-- SELECT MAX(salary) FROM Employees;

-- TASK14
-- SELECT SUM(salary) FROM Employees WHERE dept='IT';

-- TASK15
-- SELECT dept, AVG(salary) AS average_salary FROM Employees GROUP BY dept;
