CREATE DATABASE minions;

USE minions;

-- 01. Create Tables 
CREATE TABLE minions(
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(30),
age TINYINT);
 
CREATE TABLE towns(
town_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(30)); 

-- 02. Alter Minions Table 
ALTER TABLE minions 
ADD COLUMN town_id INT;

ALTER TABLE minions
ADD CONSTRAINT fk_town_id
  FOREIGN KEY (town_id)
  REFERENCES towns (id)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;
 
 -- 03. Insert Records in Both Tables
 INSERT INTO towns 
 VALUES  
 (1,'Sofia'),
 (2,'Plovdiv'),
 (3,'Varna');
 
 INSERT INTO minions 
 VALUES 
 (1,'Kevin',22,1),
 (2,'Bob',15,3),
 (3,'Steward',NULL,2);
 
 -- 04. Truncate Table Minions 
 TRUNCATE TABLE minions;
  
 -- 05.	Drop All Tables
 DROP TABLE minions;
 DROP TABLE towns;
 
 -- 06.	Create Table People
 CREATE TABLE people (
 id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
 name VARCHAR(200) NOT NULL,
 picture BLOB,
 height REAL,
 weight REAL, 
 gender CHAR NOT NULL CHECK (gender = 'm' OR gender = 'f'),
 birthdate DATE NOT NULL,
 biography TEXT
); 

INSERT INTO people 
VALUES 
(1,'Pesho','image',1.8,80,'m','1980-11-12','ffffffffffffffffffff'),
(2,'Pesho','image',1.8,80,'m','1980-11-12','ffffffffffffffffffff'),
(3,'Pesho','image',1.8,80,'m','1980-11-12','ffffffffffffffffffff'),
(4,'Pesho','image',1.8,80,'m','1980-11-12','ffffffffffffffffffff'),
(5,'Pesho','image',1.8,80,'m','1980-11-12','ffffffffffffffffffff');

-- 7. Create Table Users
-- Unicode - Database Collation should be utf8_general_ci

CREATE TABLE users (
	id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
    username VARCHAR(30) UNIQUE NOT NULL,
    password VARCHAR(26) NOT NULL,
    profile_picture BLOB,
    last_login_time DATETIME DEFAULT NOW(),
    is_deleted  TINYINT(1) CHECK(is_deleted = 1 or is_deleted = 0)
); 

INSERT INTO users 
VALUES 
(1,'pesho1','123qwe','image','1980-11-12 20:00:00',0),
(2,'pesho2','123qwe','image','1980-11-12 20:00:00',0),
(3,'pesho3','123qwe','image','1980-11-12 20:00:00',0),
(4,'pesho4','123qwe','image','1980-11-12 20:00:00',0),
(5,'pesho5','123qwe','image','1980-11-12 20:00:00',0),
(6,'pesho6','123qwe','image',NOW(),false);

-- 08.	Change Primary Key
ALTER TABLE users
DROP PRIMARY KEY,
ADD CONSTRAINT pk_users PRIMARY KEY (id,username);


-- 09.	Set Default Value of a Field
ALTER TABLE users
MODIFY COLUMN  last_login_time DATETIME DEFAULT NOW();

-- 10. Set Unique Field
ALTER TABLE users
DROP PRIMARY KEY,
ADD CONSTRAINT pk_users  PRIMARY KEY (id),
MODIFY COLUMN username  VARCHAR(30) UNIQUE NOT NULL;

-- MOVIES -------------------------------------------------------------------------------------
-- 11. Movies Database 
CREATE DATABASE Movies;
CREATE TABLE directors (
 id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
 director_name VARCHAR(50) NOT NULL, 
 notes TEXT);
 
INSERT INTO directors 
VALUES
(1,'Guillermo del Toro','He\'s a world-builder with razor sharp design and endless imagination.'),
(2,'Brian De Palma','The films of Brian De Palma are edgy — not just in their subject matter but in their presentation as well.'),
(3,'Ridley Scott','Sir Ridley Scott is an English filmmaker.'),
(4,'Christopher Nolan','He works with high budgets and high concepts — and he\'s just getting started.'),
(5,'Federico Fellini','Outside the post-war Neorealism movement, there is no Italian cinema without Federico Fellini.');

  
CREATE TABLE genres (
id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
genre_name VARCHAR(50) NOT NULL,
notes TEXT);

INSERT INTO genres 
VALUES
(1,'Thriller','Lorem ipsum'),
(2,'Romance','Lorem ipsum'),
(3,'Western','Lorem ipsum'),
(4,'Fantazy','Lorem ipsum'),
(5,'Action','Lorem ipsum');

 
CREATE TABLE categories (
id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
category_name VARCHAR(30) NOT NULL,
notes TEXT);  

INSERT INTO categories
VALUES
(1,'full-length','Lorem ipsum...'),
(2,'documentary','Lorem ipsum...'),
(3,'mini-series','Lorem ipsum...'),
(4,'animation','Lorem ipsum...'),
(5,'series','Lorem ipsum...');

CREATE TABLE movies (
id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,

title VARCHAR(100) NOT NULL,

director_id INT NOT NULL,
-- FOREIGN KEY(director_id) REFERENCES directors(id),

copyright_year DATE,

length INT,

genre_id INT NOT NULL,
-- FOREIGN KEY(genre_id) REFERENCES genres(id), 

category_id INT NOT NULL,
-- FOREIGN KEY(category_id) REFERENCES categories(id),

rating INT DEFAULT 0,

notes TEXT);
 
INSERT INTO movies
VALUES
(1,'Ho-Ho-Ho',2,"2016-01-01",120,3,1,5,"Lorem ipsum"),
(2,'Mo-Mo-MHo',4,"2016-02-02",120,3,1,5,"Lorem ipsum"),
(3,'Ra-Ra-Ra',2,"2016-03-03",120,3,1,5,"Lorem ipsum"),
(4,'Ho-Ho-Ho',2,"2016-04-04",120,3,1,5,"Lorem ipsum"),
(5,'Ho-Ho-Ho',2,"2016-05-05",120,3,1,5,"Lorem ipsum");


-- CAR RENTAL -------------------------------------------------------
-- 12.	Car Rental Database
CREATE DATABASE car_rental;

CREATE TABLE categories (
id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
category VARCHAR(100) NOT NULL,
daily_rate DOUBLE(6,2),
weekly_rate DOUBLE(6,2),
monthly_rate DOUBLE(6,2),
weekend_rate DOUBLE(6,2)
);

INSERT INTO categories (category, daily_rate, weekly_rate, monthly_rate, weekend_rate)
VALUES
('Car', 100.00,550.00,2450.00,180.00),
('Minivan', 100.00,550.00,2450.00,180.00),
('Bus', 100.00,550.00,2450.00,180.00);

CREATE TABLE cars (
id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
plate_number VARCHAR(20) NOT NULL UNIQUE,
make VARCHAR(50),
model VARCHAR(50),
car_year DATE,
category_id INT,
-- FOREIGN KEY(category_id) REFERENCES categories(id), 
doors TINYINT,
picture BLOB,
car_condition TEXT, 
available BOOL);

INSERT INTO cars (plate_number, make, model, car_year, category_id, doors, picture, car_condition, available)
VALUES
('EH4295AX','Volvo','440','1993-09-23',1,5,'test','good',true), 
('CO4295AK','Volvo','440','2003-10-19',2,4,'test','good',true),
('E4295PE','Volvo','440','2013-01-01',1,2,'test','good',true);
 

CREATE TABLE employees (
id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
first_name VARCHAR(100) NOT NULL,
last_name VARCHAR(100) NOT NULL,
title VARCHAR(100) NOT NULL,
notes TEXT);

INSERT INTO employees (first_name, last_name, title, notes)
VALUES
('Test1','Testov','Manager','Lorem ipsum ...'),
('Test2','Testov','Seller','Lorem ipsum ...'),
('Test3','Testov','Cashier','Lorem ipsum ...');

CREATE TABLE customers (
id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
driver_licence_number INT NOT NULL UNIQUE, 
full_name VARCHAR(60) NOT NULL ,
address VARCHAR(50) NOT NULL, 
city VARCHAR(60),
zip_code INT,
notes TEXT);

INSERT INTO customers (driver_licence_number, full_name, address, city, zip_code, notes)
VALUES
( 567890 ,'Ivan Ivanov 1','Konstantin and Elena 5','Plovdiv',4000,'Lorem ipsum .....'),
( 347890 ,'Ivan Ivanov 2','Konstantin and Elena 5','Plovdiv',4000,'Lorem ipsum .....'),
( 337890 ,'Ivan Ivanov 3','Konstantin and Elena 5','Plovdiv',4000,'Lorem ipsum .....');

CREATE TABLE rental_orders (
id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,

employee_id INT NOT NULL,
-- FOREIGN KEY(employee_id) REFERENCES employees(id), 
customer_id INT NOT NULL,
-- FOREIGN KEY(customer_id) REFERENCES customers(id),
car_id INT NOT NULL,
-- FOREIGN KEY(car_id) REFERENCES cars(id),

car_condition VARCHAR(255),
tank_level INT,
kilometrage_start INT,
kilometrage_end INT,
total_kilometrage INT,
start_date DATE,
end_date DATE,
total_days INT,
rate_applied DOUBLE(6,2),
tax_rate DOUBLE(6,2),
order_status BOOL,
notes TEXT);
 
INSERT INTO rental_orders (employee_id, customer_id, car_id, car_condition, tank_level, kilometrage_start, kilometrage_end, total_kilometrage, start_date, end_date, total_days, rate_applied, tax_rate, order_status, notes)
VALUES
(2,3,1,'good',60,120123,120178,55,'2024-01-03','2024-01-05',3,4.4,0.2,true,'Lorem ipsum .....'),
(1,2,3,'good',60,120123,120178,55,'2024-01-03','2024-01-05',3,4.4,0.2,true,'Lorem ipsum .....'),
(3,1,2,'good',60,120123,120178,55,'2024-01-03','2024-01-05',3,4.4,0.2,true,'Lorem ipsum .....');


-- SoftUni ---------------------------------------------------------- 
CREATE DATABASE softuni;

-- 13.	Basic Insert

CREATE TABLE towns (
id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
name VARCHAR(100) NOT NULL);

CREATE TABLE addresses (
id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
address_text TEXT,
town_id INT NOT NULL,
FOREIGN KEY(town_id) REFERENCES towns(id)
);

CREATE TABLE  departments (
id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
name VARCHAR(50) NOT NULL);

CREATE TABLE employees (
id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY, 
first_name VARCHAR(30) NOT NULL,
middle_name VARCHAR(30), 
last_name VARCHAR(30) NOT NULL,
job_title VARCHAR(30), 
department_id INT,
FOREIGN KEY(department_id) REFERENCES departments(id),
hire_date DATE,
salary FLOAT, 
address_id INT,
FOREIGN KEY(address_id) REFERENCES addresses(id)
);

INSERT INTO towns (name)
VALUES
('Sofia'), ('Plovdiv'), ('Varna'), ('Burgas');

INSERT INTO departments (name)
VALUES
('Engineering'),('Sales'),('Marketing'), ('Software Development'), ('Quality Assurance');

INSERT INTO employees (first_name,middle_name,last_name,job_title,department_id,hire_date,salary)
VALUES
('Ivan','Ivanov','Ivanov','.NET Developer',4,'2013-02-01', 3500.00),
('Petar','Petrov','Petrov','Senior Engineer',1,'2004-03-02',4000.00),
('Maria','Petrova','Ivanova','Intern',5,'2016-08-28',525.25),
('Georgi','Terziev','Ivanov','CEO',2,'2007-12-09',3000.00),
('Peter','Pan','Pan','Intern',3,'2016-08-28',599.88);

-- 14. Basic Select All Fields
SELECT * FROM towns;
SELECT * FROM departments;
SELECT * FROM employees;

-- 15. Basic Select All Fields and Order Them
SELECT * FROM towns
ORDER BY name;
SELECT * FROM departments
ORDER BY name;
SELECT * FROM employees
ORDER BY salary DESC;

-- 16.	Basic Select Some Fields 

SELECT name FROM towns
ORDER BY name;
SELECT name FROM departments
ORDER BY name;
SELECT first_name, last_name, job_title, salary FROM employees
ORDER BY salary DESC;


-- 17.	Increase Employees Salary
UPDATE employees
SET salary = salary * 1.1;
SELECT salary FROM employees;

 