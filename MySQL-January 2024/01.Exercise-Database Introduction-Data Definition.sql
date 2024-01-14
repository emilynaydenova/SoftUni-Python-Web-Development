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
 
 