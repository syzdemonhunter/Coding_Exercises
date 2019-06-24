# https://leetcode.com/problems/consecutive-numbers/

SELECT
    tmp.Num AS ConsecutiveNums
FROM
    (SELECT
        DISTINCT t1.Num 
    FROM
        Logs t1
    LEFT JOIN
        Logs t2 ON t1.Id = t2.Id - 1
    LEFT JOIN
        Logs t3 ON t1.Id = t3.Id - 2
    WHERE
        t1.Num = t2.Num and t1.Num = t3.Num) tmp

