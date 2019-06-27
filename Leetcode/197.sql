# https://leetcode.com/problems/rising-temperature/submissions/

SELECT 
    w1.Id
FROM 
    Weather w1 
INNER JOIN 
    Weather w2 ON TO_DAYS(w1.RecordDate) = TO_DAYS(w2.RecordDate) + 1
WHERE 
    w1.Temperature > w2.Temperature
;
