/*
PostgreSQL is a case-sensitive database by default,
but provides various possibilities for performing case-insensitive
operations and working with collations.
*/
-- 00. Create a Database
CREATE DATABASE IF NOT EXISTS minions_db;
 
--  01. Create a Table
CREATE TABLE IF NOT EXISTS minions (
    id SERIAL PRIMARY KEY,    
    name varchar(30),
    age INTEGER
);
 
--  02. Rename the table
ALTER TABLE minions
RENAME TO minions_info;
-- ALTER TABLE table_name RENAME TO new_table_name;

-- 03. Alter the Table - add new fields
ALTER TABLE minions_info
ADD COLUMN code CHAR(4),
ADD COLUMN task TEXT,
ADD COLUMN salary DECIMAL(8,3);
-- ALTER TABLE [schema_name.]table_name 
-- ADD COLUMN <column_name> <data_type> [column_constraint];  

-- 04. Rename Column
ALTER TABLE minions_info
RENAME COLUMN salary TO banana;
-- ALTER TABLE [schema_name.]table_name 
-- RENAME COLUMN <column_name> to <new_column_name> 

-- 05. Add New Columns
ALTER TABLE minions_info
ADD COLUMN email VARCHAR(20),
ADD COLUMN equipped BOOLEAN NOT NULL; -- DEFAULT False 
-- PostgreSQL offers three states of BOOLEAN data type: TRUE, FALSE, or NULL

!!!  add DEFAULT value when adding column  if already have records in this table

-- 06. Create ENUM Type https://www.postgresql.org/docs/16/datatype-enum.html
CREATE TYPE type_mood
 AS ENUM (
    'happy',
    'relaxed',
    'stressed',
    'sad'
    );
ALTER TABLE minions_info
ADD COLUMN mood type_mood;

-- CREATE custom type of data
/*
CREATE TYPE address AS (
    street varchar(60),
    city varchar(30),
    postal_code int(4)
);

CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    customer_name VARCHAR(50),
    customer_address address,
);

INSERT INTO 
    customers (customer_name, customer_address)
VALUES ('Ivan', ('some street','some city',1616));

*/
--07. Set Default -> works for next records
ALTER TABLE minions_info
ALTER COLUMN age SET DEFAULT 0,
ALTER COLUMN "name" SET DEFAULT '',
ALTER COLUMN code SET DEFAULT '';

-- 08. Add Constraints
-- ALTER TABLE <table_name>
-- ADD CONSTRAINT <constraint_name> <constraint_definition> (<column1>, <column2>, ... <column_n>);

ALTER TABLE minions_info
ADD CONSTRAINT unique_containt UNIQUE (id,email),  /* better to name UQ_email_and_id */
ADD CONSTRAINT banana_check CHECK(banana > 0);    /* CK_banana_is_positive */

-- 09.	Change Column’s Data Type
ALTER TABLE minions_info
ALTER COLUMN task [SET DATA] TYPE VARCHAR(150);

-- 10. Drop Constraint
ALTER TABLE minions_info
ALTER COLUMN equipped DROP NOT NULL;

-- 11. Remove Column
ALTER TABLE minions_info
DROP COLUMN age;

--12. Table Birthdays
CREATE TABLE minions_birthdays (
	id INTEGER UNIQUE NOT NULL,
	name VARCHAR(50),
	date_of_birth DATE,
	age INTEGER,
	present VARCHAR(100),
	party TIMESTAMPTZ
);

-- 13.	Insert Into  -> instances
INSERT INTO minions_info 
	(name, code, task, banana, email, equipped, mood)
VALUES 
	('Mark', 'GKYA', 'Graphing Points', 3265.265, 'mark@minion.com', false, 'happy'),
	('Mel', 'HSK', 'Science Investigation', 54784.996, 'mel@minion.com', true, 'stressed'),
	('Bob', 'HF', 'Painting', 35.652, 'bob@minion.com', true, 'happy'),
	('Darwin', 'EHND', 'Create a Digital Greeting', 321.958, 'darwin@minion.com', false, 'relaxed'),
	('Kevin', 'KMHD', 'Construct with Virtual Blocks', 35214.789, 'kevin@minion.com', false, 'happy'),
	('Norbert', 'FEWB', 'Testing', 3265.500, 'norbert@minion.com', true, 'sad'),
	('Donny', 'L', 'Make a Map', 8.452, 'donny@minion.com', true, 'happy');

-- 14.* Select
SELECT name,task,email,banana
FROM minions_info;

-- 15. Truncate the Table
TRUNCATE TABLE minions_info;

SELECT name,task,email,banana
FROM minions_info;

-- 16. Drop the Table
DROP TABLE minions_birthdays;

-- 17.	Drop the Database
DROP DATABASE minions_db WITH (FORCE);
