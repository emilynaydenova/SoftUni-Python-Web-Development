USE SoftUni
GO

--- Problem 02.
SELECT * 
FROM Departments

--- Problem 03.
SELECT [Name]
FROM Departments

--- Problem 04.
SELECT FirstName, LastName, Salary
FROM Employees

--- Problem 05.
SELECT FirstName, MiddleName, LastName
FROM Employees

--- Problem 06.
SELECT CONCAT(FirstName,'.',LastName,'@softuni.bg') AS [Full Email Address] 
FROM Employees

--- Problem 07.
SELECT DISTINCT Salary
FROM Employees
 

--- Problem 08.
SELECT *
FROM Employees
WHERE JobTitle = 'Sales Representative'

--- Problem 09.
SELECT FirstName,LastName,JobTitle
FROM Employees 
WHERE Salary BETWEEN 20000 AND 30000


--- Problem 10.
-- SELECT CONCAT_WS(' ',FirstName,MiddleName, LastName) AS [Full Name]
-- SELECT REPLACE(CONCAT(FirstName+' ',MiddleName+' ',LastName+' '),'  ',' ') AS [Full Name]
SELECT CONCAT(FirstName,' ',MiddleName,' ',LastName) AS [Full Name]
FROM Employees
WHERE Salary in (25000, 14000, 12500, 23600)

--- Problem 11.
SELECT FirstName, LastName
FROM Employees
WHERE ManagerID IS NULL

--- Problem 12.
SELECT FirstName, LastName, Salary
FROM Employees
WHERE Salary > 50000
ORDER BY Salary DESC

--- Problem 13.
SELECT TOP(5) FirstName, LastName
FROM Employees
ORDER BY Salary DESC

--- Problem 14.
SELECT FirstName, LastName
FROM Employees
WHERE DepartmentID <> 4


--- Problem 15.
SELECT * 
FROM Employees
ORDER BY Salary DESC, FirstName, LastName DESC, MiddleName

GO
--- Problem 16.
CREATE VIEW V_EmployeesSalaries 
AS
SELECT FirstName,LastName,Salary
FROM Employees

GO
--
SELECT * FROM V_EmployeesSalaries
DROP View V_EmployeesSalaries  -- for delete

GO
--- Problem 17.
CREATE VIEW V_EmployeeNameJobTitle 
AS
--SELECT CONCAT_WS(' ',FirstName,MiddleName,LastName) AS [Full Name], JobTitle AS [Job Title]
SELECT CONCAT(FirstName,' ',ISNULL(MiddleName,''),' ',LastName) AS [Full Name],
	JobTitle AS [Job Title]
FROM Employees

GO
SELECT * FROM V_EmployeeNameJobTitle

--- Problem 18.
SELECT DISTINCT JobTitle
FROM Employees

--- Problem 19.
SELECT TOP(10) * 
FROM Projects
ORDER BY StartDate, [Name]


-- Problem 20.
SELECT TOP(7) FirstName, LastName, HireDate 
FROM Employees
ORDER BY HireDate DESC


--- Problem 21.  !!!!
UPDATE table1
SET table1.c1 = ....,
    table1.c2 = expression,
    ...   
FROM table1
     [INNER | LEFT] JOIN table2 ON join_predicate
WHERE 
    where_predicate;

 -- Backup SoftUni 


UPDATE Employees
SET Salary *= 1.12
FROM Employees e
JOIN Departments d ON e.DepartmentID = d.DepartmentID
WHERE d.[Name] IN ('Engineering', 'Tool Design', 'Marketing', 'Information Services') 
SELECT Salary FROM Employees;
 
---
--- Restore SoftUni

-- Problem 22.
USE Geography
GO

SELECT PeakName
FROM Peaks
ORDER BY PeakName

-- Problen 23.
SELECT TOP(30) CountryName,Population
FROM Countries
WHERE ContinentCode = 'EU'
ORDER BY [Population] DESC


--- Problem 24.
SELECT CountryName, CountryCode,
   'Currency' =
    CASE 
	  WHEN CurrencyCode = 'EUR' THEN 'Euro'
	  ELSE 'Not Euro'
	END
FROM Countries
ORDER BY CountryName
 

 /*SELECT ProductNumber, Name, "Price Range" = 
  CASE 
     WHEN ListPrice =  0 THEN 'Mfg item - not for resale'
     WHEN ListPrice < 50 THEN 'Under $50'
     WHEN ListPrice >= 50 and ListPrice < 250 THEN 'Under $250'
     WHEN ListPrice >= 250 and ListPrice < 1000 THEN 'Under $1000'
     ELSE 'Over $1000'
  END
FROM Production.Product
ORDER BY ProductNumber ;*/

GO 

-- Problem 25.
USE Diablo
GO
SELECT [Name] FROM Characters
ORDER BY [Name]