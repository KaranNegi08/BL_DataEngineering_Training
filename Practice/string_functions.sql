--STRING FUNCTIONS--

-- 1. CONCAT()
-- SELECT CONCAT('hello',' world')
-- SELECT emp_id, CONCAT(fname , ' ',lname) as full_name FROM Employees


-- 2. CONCAT_WS()
-- SELECT CONCAT_WS(' : ', 'One','Two','Three')

-- 3. SUBSTRING
-- SELECT SUBSTR('Hello Buddy',1,8)

 -- 4.REPLACE --
 -- SELECT REPLACE('ASDCCBFD','DC','KN')
 -- SELECT REPLACE(dept,'IT','TECH') from Employees;

 -- 5.REVERSE --
 -- SELECT REVERSE('Hello');

 -- 6.LENGTH --
 -- SELECT fname FROM Employees WHERE LENGTH(fname) > 4;

 -- 7.UPPER & LOWER
 -- SELECT UPPER(fname) from Employees;
  -- SELECT LOWER(fname) from Employees;

-- 8.LEFT & RIGHT--
-- SELECT LEFT(fname,4) FROM Employees;
-- SELECT Right(fname,4) FROM Employees;

-- 9.TRIM --
-- SELECT LENGTH(TRIM('   HELLO    '))

-- 9.POSITION
-- SELECT POSITION('a' IN fname) FROM Employees;
