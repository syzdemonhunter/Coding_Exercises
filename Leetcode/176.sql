# https://leetcode.com/problems/second-highest-salary/

SELECT
    max(Salary) AS SecondHighestSalary 
FROM
    Employee
WHERE Salary < 
    (SELECT 
        max(Salary)
     FROM
        Employee)
;