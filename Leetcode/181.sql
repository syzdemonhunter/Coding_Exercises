# https://leetcode.com/problems/employees-earning-more-than-their-managers/

SELECT
	e1.Name AS Employee
FROM
	Employee e1 
LEFT JOIN Employee e2 ON e1.ManagerId = e2.Id 
WHERE
	e1.ManagerId is NOT NULL AND e1.Salary > e2.Salary
;
