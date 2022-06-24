-- Write your Queries here
-- 1. Find the employee being paid the most
SELECT first_name, last_name FROM employees ORDER BY annual_salary DESC LIMIT 1;

-- 2. Find the employee being paid the least
SELECT first_name, last_name FROM employees ORDER BY annual_salary LIMIT 1;

-- 3. Find the department with the highest average salary
SELECT department FROM employees GROUP BY department ORDER BY AVG(annual_salary) DESC LIMIT 1;

-- 4. Find the department with the lowest average salary
SELECT department FROM employees GROUP BY department ORDER BY AVG(annual_salary) LIMIT 1;

-- 5. Find the average salary difference between full time and part time workers
SELECT (SELECT AVG(annual_salary) FROM employees WHERE full_or_part_time = 'F') - (SELECT AVG(annual_salary) FROM employees WHERE full_or_part_time = 'P') AS difference;

-- 6. Find the most common first name
SELECT first_name, count(first_name) FROM employees GROUP BY first_name ORDER BY count(first_name) DESC LIMIT 1;

-- 7. Find the most common last name
SELECT last_name, count(last_name) FROM employees GROUP BY last_name ORDER BY count(last_name) DESC LIMIT 1;

-- 8. If there are people with the same name, find what their job titles, departments, and annual salaries are
SELECT first_name, last_name, job_title, department, annual_salary FROM employees WHERE CONCAT(first_name, ' ', last_name) IN (SELECT name FROM (SELECT CONCAT(first_name, ' ', last_name) as name, COUNT(*) FROM employees GROUP BY 1 HAVING COUNT(*) > 1) AS subquery ORDER BY name);