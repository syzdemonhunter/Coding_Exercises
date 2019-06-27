# https://leetcode.com/problems/game-play-analysis-iv/

SELECT
    ROUND(SUM(CASE WHEN t1.first_login + 1 = t2.event_date THEN 1 ELSE 0 END) /
    COUNT(DISTINCT t1.player_id), 2) AS fraction
FROM
    (SELECT
        player_id
        , MIN(event_date) AS first_login
    FROM
        Activity t1
    GROUP BY 1) t1
JOIN
    Activity t2 on t1.player_id = t2.player_id
;

