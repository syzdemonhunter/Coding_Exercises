# https://leetcode.com/problems/get-highest-answer-rate-question/

SELECT
    MAX(t.question_id) as survey_log
FROM
    (SELECT
        question_id
    FROM
        survey_log
    WHERE
        answer_id IS NOT NULL) t
GROUP BY
    t.question_id
ORDER BY
    COUNT(*) DESC
LIMIT 1
;

