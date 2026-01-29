--Find employees earning more than average salary
SELECT emp_name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

--Find department with highest total salary
SELECT d.dept_name, SUM(e.salary) AS total_salary
FROM employees e
JOIN departments d
ON e.dept_id =  d.dept_id
GROUP BY d.dept_name
HAVING SUM(e.salary) = (
	SELECT MAX(dept_total)
	FROM (
        SELECT SUM(salary) AS dept_total
		FROM employees
		GROUP BY dept_id
		)t
	);

--Display employee with second highest salary
SELECT emp_name, salary
FROM employees 
WHERE salary = (
    SELECT MAX(salary)
	FROM employees 
	WHERE salary < (SELECT MAX(salary) FROM employees)
);

--Display employees working in the same department as "YASH"
SELECT emp_name
FROM employees
WHERE dept_id = (
    SELECT dept_id
	FROM employees
	WHERE emp_name = 'Yash'
);