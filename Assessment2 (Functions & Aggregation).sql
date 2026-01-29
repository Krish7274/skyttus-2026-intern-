--Count Total Number Of Students..
SELECT COUNT(*) AS total_student FROM student;

--Find Average Marks of students..
SELECT AVG(marks) AS average_marks FROM student;

--Find Highest and Lowest MArks..
SELECT MAX(marks) AS highest_marks, MIN(marks) AS lowest_marks FROM student;

--FInd department-wise average marks..
SELECT department, AVG(marks) AS avg_marks FROM student  GROUP BY department; 

--Display department where average marks > 70..
SELECT department, AVG(marks) AS avg_marks FROm Student GROUP BY department HAVING AVG(marks) > 70;