# https://leetcode.com/problems/game-play-analysis-ii/

SELECT
    t1.player_id
    , t1.device_id
FROM
    Activity t1
INNER JOIN
    (SELECT
        player_id
        , MIN(event_date) AS first_login
    FROM
        Activity
    GROUP BY
        player_id) t2
ON t1.event_date = t2.first_login AND t1.player_id = t2.player_id
;
