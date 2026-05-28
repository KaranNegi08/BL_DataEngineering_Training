-- CREATE TABLE person(
-- 	person_id SERIAL PRIMARY KEY,
-- 	name VARCHAR(50)  NOT NULL,
-- 	age INT NOT NULL
-- );

-- ALTER TABLE person ADD dept VARCHAR(50) DEFAULT 'IT'; 

-- SELECT * FROM person;

-- INSERT INTO person(name,age) VALUES('KK bhai ',20)


-- ALTER TABLE person DROP COLUMN dept;
-- ALTER TABLE person RENAME COLUMN name TO fname;

-- ALTER TABLE person RENAME TO myPerson;
-- SELECT * FROM myPerson

-- ALTER TABLE myPerson ALTER COLUMN fname SET DATA TYPE VARCHAR(150);

-- ALTER TABLE myPerson ADD COLUMN mob VARCHAR(15) CHECK (LENGTH(mob) >= 10)
-- INSERT INTO myPerson(fname,mob,age) VALUES ('Vishal',1245897563,25)
-- ALTER TABLE myPerson ADD CONSTRAINT mob_no_less_than_10 CHECK (LENGTH(mob) >= 10)
