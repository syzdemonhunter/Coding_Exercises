# https://leetcode.com/problems/game-play-analysis-i/submissions/

SELECT
    player_id
    , MIN(event_date) AS first_login
FROM
    Activity
GROUP BY
    player_id
;

