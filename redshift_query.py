# -- CREATE DATABASE mydb;
# -- SELECT *  FROM pg_database;
# -- CREATE USER myuser PASSWORD 'Myuser123';
# -- SELECT * FROM pg_user;
# -- SELECT current_user;
# -- CREATE SCHEMA myschema AUTHORIZATION myuser;
# -- SELECT * FROM pg_namespace;

# -- CREATE TABLE myschema.emp(
# --     empID int,
# --     City varchar (255)
# -- );
# -- GRANT SELECT ON ALL TABLES IN SCHEMA myschema TO myuser;
# -- GRANT ALL ON SCHEMA myschema TO myuser;
# -- SHOW search_path;
# -- SET search_path to '$user','public','myschema';
# SELECT * FROM pg_table_def where schemaname='myschema';


# -- ABORT or ROLLBACK;
# -- CREATE TABLE myschema.venue(
# --     id smallint not null distkey sortkey,
# --     name varchar(100),
# --     city varchar(30),
# --     state char(2),
# --     seats integer
# -- );

# -- COPY dev.myschema.venue FROM 's3://redshift-demo-24/venue.csv' IAM_ROLE 'arn:aws:iam::984445750718:role/redshift-custom-role' FORMAT AS CSV DELIMITER ',' QUOTE '"' IGNOREHEADER 1 REGION AS 'us-east-1'
# -- SELECT * FROM myschema.venue
# -- UNLOAD('SELECT * FROM dev.myschema.venue')  TO 's3://redshift-demo-24/output/' IAM_ROLE 'arn:aws:iam::984445750718:role/redshift-custom-role' CSV PARALLEL OFF;
 
# --  CREATE EXTERNAL SCHEMA spectrum_schema FROM DATA CATALOG DATABASE 'mydatabase'
# --  IAM_ROLE 'arn:aws:iam::984445750718:role/redshift-custom-role'
# --  CREATE EXTERNAL DATABASE IF NOT EXISTS;

# -- ALTER schema spectrum_schema owner to myuser;

# -- CREATE EXTERNAL TABLE spectrum_schema.venue(
# --     id smallint,
# --     name varchar(100),
# --     city varchar(30),
# --     state char(2),
# --     seats integer
# -- )
# -- ROW FORMAT DELIMITED 
# -- FIELDS TERMINATED BY ','
# -- LOCATION 's3://redshift-demo-24/'

# -- SELECT * FROM spectrum_schema.venue;

# -- CREATE OR REPLACE  PROCEDURE myschema.test_api(f1 int, f2 varchar(20))
# -- AS $$
# -- DECLARE 
# --     min_val int;
# -- BEGIN
# --     DROP TABLE IF EXISTS tmp_tb1;
# --     CREATE TEMP TABLE tmp_tb1(id int);
# --     INSERT INTO tmp_tb1 values (f1);
# --     SELECT INTO min_val MIN(id) FROM tmp_tb1;
# --     RAISE INFO 'min_val = %, f2 = %', min_val,f2;
# -- END;
# -- $$ LANGUAGE plpgsql;

# CALL myschema.test_api(10,'test_param');

