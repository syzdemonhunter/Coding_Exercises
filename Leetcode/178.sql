# https://leetcode.com/problems/rank-scores/
# https://www.youtube.com/watch?v=3wR007rPf5M

SELECT
    s1.Score AS Score
    , (SELECT
           COUNT(DISTINCT s2.Score)
       FROM 
           Scores s2
       WHERE
           s2.Score > s1.Score) + 1 AS Rank
FROM
    Scores s1
ORDER BY
    s1.Score DESC
