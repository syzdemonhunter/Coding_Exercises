# https://leetcode.com/problems/nth-highest-salary/

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
DECLARE M INT;
SET M = N - 1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT
        Salary 
      FROM 
        Employee
      GROUP BY
        Salary
      ORDER BY
        Salary DESC
      LIMIT
        M, 1
  );
END