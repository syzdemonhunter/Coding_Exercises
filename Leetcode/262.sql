# https://leetcode.com/problems/trips-and-users/

SELECT Request_at AS Day
       , ROUND(SUM(IF(Status = 'completed', 0, 1))/COUNT(*), 2) AS 'Cancellation Rate'
FROM
    (SELECT
        t.Client_Id
        , t.Status
        , t.Request_at
    FROM 
        Trips t
    LEFT JOIN
        Users u ON t.Client_Id = u.Users_Id
    WHERE
        u.Banned = 'No' AND 
        t.Request_at >= '2013-10-01' AND 
        t.Request_at <= '2013-10-03') tmp
GROUP BY
    Request_at
;

