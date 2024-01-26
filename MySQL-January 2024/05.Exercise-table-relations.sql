CREATE DATABASE relations;
USE relations;
-- 1.	One-To-One Relationship
CREATE TABLE passports (
    passport_id INT AUTO_INCREMENT PRIMARY KEY,
    `passport_number` VARCHAR(30) NOT NULL
);

-- start value of id if id!= 1
ALTER TABLE passports AUTO_INCREMENT=101;

CREATE TABLE people (
    person_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(30) NOT NULL,
    salary DECIMAL(10 , 2 ),
    passport_id INT UNIQUE,
    FOREIGN KEY (passport_id)
        REFERENCES passports (passport_id)
);

INSERT INTO passports (`passport_number`)
VALUES
('N34FG21B'),
('K65LO4R7'),
('ZE657QP2');

INSERT INTO people (`first_name`,`salary`,`passport_id`)
VALUES
('Roberto',	43300.00, 102),
('Tom',	56100.00, 103),
('Yana', 60200.00, 101);
	


-- 2.	One-To-Many Relationship
CREATE TABLE manufacturers (
    manufacturer_id INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(30) NOT NULL,
    `established_on` DATE
);

CREATE TABLE models (
    model_id INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(30) NOT NULL,
    manufacturer_id INT,
    CONSTRAINT fk_models_manufacturers FOREIGN KEY (manufacturer_id)
        REFERENCES manufacturers (manufacturer_id)
);

INSERT INTO manufacturers (name,established_on)
VALUES  
  	('BMW', 	'1916-03-01'),
	('Tesla',	'2003-01-01'),
    ('Lada',	'1966-05-01');
 
INSERT INTO models 
VALUES
(101,'X1',1),
(102,'i6',1),
(103,'Model S',	2),
(104,'Model X',	2),
(105,'Model 3',	2),
(106,'Nova',3);


-- 3.	Many-To-Many Relationship

CREATE TABLE students (
student_id INT AUTO_INCREMENT PRIMARY KEY,
`name` VARCHAR(30) NOT NULL);

CREATE TABLE exams (
exam_id INT AUTO_INCREMENT PRIMARY KEY,
`name` VARCHAR(30) NOT NULL);

ALTER TABLE exams AUTO_INCREMENT=101;

CREATE TABLE students_exams (
    student_id INT NOT NULL,
    exam_id INT NOT NULL,
    CONSTRAINT pk_students_exams PRIMARY KEY (student_id , exam_id),
    FOREIGN KEY (student_id)
        REFERENCES students (student_id),
    FOREIGN KEY (exam_id)
        REFERENCES exams (exam_id)
);


INSERT INTO students (`name`)
VALUES
('Mila'),                                  
('Toni'),
('Ron');

INSERT INTO exams (`name`)
VALUES
("Spring MVC"),
("Neo4j"),
("Oracle 11g");

INSERT INTO students_exams (`student_id`,`exam_id`)
VALUES
(1,	101),
(1,	102),
(2,	101),
(3,	103),
(2,	102),
(2,	103); 

-- 4.	Self-Referencing
CREATE TABLE teachers (
teacher_id  INT AUTO_INCREMENT PRIMARY KEY,
`name` VARCHAR(30) NOT NULL,
manager_id INT,
FOREIGN KEY(manager_id)  REFERENCES teachers(teacher_id)
);

ALTER TABLE teachers AUTO_INCREMENT=101;


INSERT INTO teachers (`name`) 
VALUES 
('John'),	
('Maya'),
('Silvia'),
('Ted'),
('Mark'),
('Greta');

UPDATE teachers 
SET `manager_id`= 101 
WHERE teacher_id IN (105,106);

UPDATE teachers 
SET `manager_id`= 105 
WHERE teacher_id=104;

UPDATE teachers 
SET `manager_id`= 106 
WHERE teacher_id IN (102,103);

-- 5.	Online Store Database
CREATE DATABASE ONLINE_STORE;

CREATE TABLE cities (
    city_id INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(50) NOT NULL
);

CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(50) NOT NULL,
    birthday DATE,
    city_id INT,
    FOREIGN KEY (city_id)
        REFERENCES cities (city_id)
);

CREATE TABLE item_types (
    item_type_id INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(50) NOT NULL
);

CREATE TABLE items (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(50) NOT NULL,
    item_type_id INT,
    FOREIGN KEY (item_type_id)
        REFERENCES item_types (item_type_id)
);

CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    FOREIGN KEY (customer_id)
        REFERENCES customers (customer_id)
);

CREATE TABLE order_items (
    order_id INT,
    item_id INT,
    PRIMARY KEY (order_id , item_id),
    FOREIGN KEY (order_id)
        REFERENCES orders (order_id),
    FOREIGN KEY (item_id)
        REFERENCES items (item_id)
);

-- 6.	University Database
CREATE DATABASE university;
USE university;

CREATE TABLE majors (
    major_id INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(50)
);

CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    student_number VARCHAR(12) NOT NULL,
    student_name VARCHAR(50) NOT NULL,
    major_id INT,
    FOREIGN KEY (major_id)
        REFERENCES majors (major_id)
);

CREATE TABLE subjects (
    subject_id INT AUTO_INCREMENT PRIMARY KEY,
    subject_name VARCHAR(50) NOT NULL
);

CREATE TABLE agenda (
    student_id INT,
    subject_id INT,
    PRIMARY KEY (student_id , subject_id),
    FOREIGN KEY (student_id)
        REFERENCES students (student_id),
    FOREIGN KEY (subject_id)
        REFERENCES subjects (subject_id)
);

CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    payment_date DATE,
    payment_amount DECIMAL(8 , 2 ),
    student_id INT,
    FOREIGN KEY (student_id)
        REFERENCES students (student_id)
);


-- 9.	Peaks in Rila
SELECT 
    m.mountain_range, p.peak_name, p.elevation AS peak_elevation
FROM
    peaks AS p
        JOIN
    mountains AS m ON p.mountain_id = m.id
WHERE
    m.mountain_range = 'Rila'
ORDER BY p.elevation DESC




