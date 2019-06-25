# https://leetcode.com/problems/department-top-three-salaries/

SELECT 
    D.Name AS Department
    , E.Name AS Employee
    , E.Salary AS Salary
FROM 
    Employee E
LEFT JOIN
    Department D ON E.DepartmentId = D.Id
WHERE (
    SELECT 
        COUNT(DISTINCT(Salary))
    FROM 
        Employee
    WHERE 
        DepartmentId = E.DepartmentId AND Salary > E.Salary
    ) < 3
AND D.Id IS NOT NULL
ORDER BY 
    E.DepartmentId, E.Salary DESC;

