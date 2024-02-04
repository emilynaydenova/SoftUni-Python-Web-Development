USE soft_uni;
-- 01.	Employees with Salary Above 35000
DELIMITER $$
-- for Judge without DELIMITER
CREATE PROCEDURE usp_get_employees_salary_above_35000()
BEGIN
	SELECT first_name, last_name
    FROM employees
    WHERE salary > 35000
    ORDER BY first_name, last_name, employee_id;

END $$

DELIMITER ;
CALL usp_get_employees_salary_above_35000();

-- 02.	Employees with Salary Above Number
DELIMITER $$
CREATE PROCEDURE usp_get_employees_salary_above(rate DECIMAL(16,4))
BEGIN
	SELECT first_name, last_name
    FROM employees
    WHERE salary >= rate
    ORDER BY first_name, last_name, employee_id;
END $$

DELIMITER ;
CALL usp_get_employees_salary_above(45000);


-- 03.	Town Names Starting With
DELIMITER //
CREATE PROCEDURE usp_get_towns_starting_with(str VARCHAR(30))
BEGIN
	SELECT name AS 'town_name'
    FROM towns
	WHERE `name` LIKE CONCAT(str,'%')
    ORDER BY town_name;
END //

DELIMITER ;
CALL usp_get_towns_starting_with('b');


-- 04.	Employees from Town
DELIMITER //
CREATE PROCEDURE usp_get_employees_from_town(town_name VARCHAR(50))
BEGIN
 	SELECT e.first_name, e.last_name FROM employees AS e
    JOIN addresses AS a ON e.address_id = a.address_id
    JOIN towns AS t ON t.town_id = a.town_id
    WHERE t.name = town_name
    ORDER BY e.first_name, e.last_name, e.employee_id;
END //

DELIMITER ;
CALL usp_get_employees_from_town('Sofia');

-- 05.	Salary Level Function
DELIMITER //
CREATE function ufn_get_salary_level(salary DECIMAL(16,4))
RETURNS VARCHAR(20)
DETERMINISTIC
BEGIN
	DECLARE result VARCHAR(20);
    IF salary >= 0 AND salary < 30000 THEN
		SET result = 'Low';
	ELSEIF salary <= 50000 THEN
		SET result = 'Average';
	ELSEIF salary > 50000 THEN
		SET result = 'High';
	END IF;
    RETURN result;
END //

DELIMITER ;
SELECT ufn_get_salary_level(13500);
SELECT ufn_get_salary_level(43300);
SELECT ufn_get_salary_level(125500);

-- 06.	Employees by Salary Level
DELIMITER //
CREATE PROCEDURE usp_get_employees_by_salary_level (salary_level VARCHAR(20))
BEGIN
	SELECT first_name, last_name
    FROM employees
    WHERE salary_level = ufn_get_salary_level(salary)
    ORDER BY first_name DESC, last_name DESC;
END //

DELIMITER ;
CALL usp_get_employees_by_salary_level ('High');


-- 07.	Define Function
DELIMITER //
CREATE FUNCTION ufn_is_word_comprised(set_of_letters varchar(50), word varchar(50))  
RETURNS TINYINT
DETERMINISTIC
BEGIN
    RETURN LOWER(word) REGEXP CONCAT('^[',set_of_letters,']+$');
END //
 
DELIMITER ;
SELECT ufn_is_word_comprised('oistmiahf',  'Sofia');
SELECT ufn_is_word_comprised('oistmiahf',  'halves');
SELECT ufn_is_word_comprised('bobr',  'Rob');
SELECT ufn_is_word_comprised('pppp',  'Sofia');

 
-- run bank_db.sql
-- 08.	Find Full Name
DELIMITER $$
CREATE PROCEDURE usp_get_holders_full_name() 
BEGIN
	SELECT CONCAT_WS(' ',first_name,last_name) AS full_name
    FROM account_holders
    ORDER BY full_name, id;
END $$

DELIMITER ;
CALL usp_get_holders_full_name();

-- 09.	People with Balance Higher Than
DELIMITER $$
CREATE PROCEDURE usp_get_holders_with_balance_higher_than(num DOUBLE) 
BEGIN
	SELECT ah.first_name,ah.last_name
	FROM account_holders AS ah
	JOIN accounts AS a ON a.account_holder_id = ah.id
	GROUP BY ah.id
	HAVING SUM(a.balance) > num
	ORDER BY ah.id;
END $$

DELIMITER ;
CALL usp_get_holders_with_balance_higher_than(7000);
 
 
 -- 10.	Future Value Function
DELIMITER //
CREATE FUNCTION ufn_calculate_future_value(
			amount DECIMAL(16,4), 
            interest DECIMAL(6,4),
            num_of_years INT)
         
RETURNS DECIMAL(16,4)
DETERMINISTIC
BEGIN
	DECLARE result DECIMAL(16,4);
    SET result = POW(1+interest,num_of_years) * amount;
    RETURN result;
END //
 
DELIMITER ;
SELECT  ufn_calculate_future_value(1000, 0.5, 5);
SELECT  ufn_calculate_future_value(1000, 0, 5);

-- 11.	Calculating Interest
DELIMITER $$
CREATE PROCEDURE usp_calculate_future_value_for_account (acc_id INT, irate DECIMAL(10,4))
BEGIN
	SELECT a.id AS account_id,
           ah.first_name,
		   ah.last_name,
		   a.balance AS current_balance,
           ufn_calculate_future_value(a.balance,irate,5) AS balance_in_5_years
    FROM accounts AS a
    JOIN account_holders AS ah ON a.account_holder_id = ah.id
    WHERE a.id = acc_id;
END $$

DELIMITER ;
CALL usp_calculate_future_value_for_account (1, 0.1);


-- 12.	Deposit Money
DELIMITER //
CREATE PROCEDURE usp_deposit_money(account_id INT, money_amount DECIMAL(16,4)) 
BEGIN
	START TRANSACTION;
    IF money_amount >= 0 THEN
		UPDATE accounts
        SET balance = balance + money_amount
        WHERE id = account_id;
		COMMIT;
	ELSE ROLLBACK;
    END IF;
END //

DELIMITER ;
CALL usp_deposit_money(1, 10);
CALL usp_deposit_money(1, -10);

-- 13.	Withdraw Money
DELIMITER //
CREATE PROCEDURE usp_withdraw_money(account_id INT, money_amount DECIMAL(16,4)) 
BEGIN
DECLARE acc_balance DECIMAL(16,4);
START TRANSACTION;  
	SELECT balance INTO acc_balance
    FROM accounts as a
    WHERE a.id = account_id;
     
    IF money_amount < 0 OR acc_balance < money_amount 
		THEN ROLLBACK;
    ELSE
		UPDATE accounts AS a
		SET balance = balance - money_amount
		WHERE a.id = account_id;
		COMMIT;
	END IF;	
END //

DELIMITER ;
CALL usp_withdraw_money(1, 10);
CALL usp_withdraw_money(1, 210);
CALL usp_withdraw_money(1, -10);

-- 14.	Money Transfer
DELIMITER //
CREATE PROCEDURE usp_transfer_money(from_account_id INT, to_account_id INT, amount DECIMAL(16,4)) 
BEGIN
	START TRANSACTION;
	IF amount < 0 
    OR 
	(SELECT COUNT(*) FROM accounts AS a WHERE a.id=from_account_id) != 1
    OR
    (SELECT COUNT(*) FROM accounts AS a WHERE a.id=to_account_id) != 1
    OR
    (SELECT a.balance FROM accounts AS a WHERE a.id=from_account_id) < amount
	THEN ROLLBACK;
    ELSE
		UPDATE accounts as a
		SET balance = balance - amount
		WHERE a.id = from_account_id;
		
		UPDATE accounts as a
		SET balance = balance + amount
		WHERE a.id = to_account_id;
	 
		COMMIT;
    END IF;
END //

DELIMIT;
CALL usp_transfer_money(1,2,10);
CALL usp_transfer_money(1,2,210);
CALL usp_transfer_money(1,2,-10);

-- 15.	Log Accounts Trigger

CREATE TABLE logs(
log_id INT AUTO_INCREMENT PRIMARY KEY,
account_id INT , 
old_sum DECIMAL(16,4),
new_sum DECIMAL(16,4)
);

DELIMITER //
CREATE TRIGGER tr_update_accounts AFTER UPDATE ON accounts
FOR EACH ROW
BEGIN
	INSERT INTO logs (account_id, old_sum, new_sum)
	VALUES(
		OLD.id,
        OLD.balance,
        NEW.balance
        ); 
END//

DELIMITER ;
SELECT * FROM logs;

-- 16.	Emails Trigger
CREATE TABLE notification_emails (
    id INT AUTO_INCREMENT PRIMARY KEY,
    recipient INT,
    subject VARCHAR(50),
    body VARCHAR(200)
);
 
DELIMITER //
CREATE TRIGGER tr_insert_logs AFTER INSERT ON `logs`
FOR EACH ROW
BEGIN
	DECLARE subject_text VARCHAR(100);
    DECLARE body_text VARCHAR(200);
    
    SET subject_text = CONCAT("Balance change for account: ",new.account_id);
    SET body_text = CONCAT("On ",
						DATE_FORMAT(NOW(),"%b %d %Y at %r"),
                        " your balance was changed from ",
						new.old_sum,
						" to ",
                        new.new_sum,
                        ".");
                
	INSERT INTO notification_emails(recipient, subject, body)
	VALUES(
		new.account_id,
        subject_text,
        body_text
        ); 
END //

DELIMITER ;
CALL usp_transfer_money(1,2,10);
SELECT * FROM logs;
SELECT * FROM notification_emails; 
