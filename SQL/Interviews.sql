/* https://www.hackerrank.com/challenges/interviews/problem */

WITH Total_View_Stats AS (
    SELECT
        challenge_id,
        SUM(total_views) AS total_views,
        SUM(total_unique_views) AS total_unique_views
    FROM View_Stats
    GROUP BY challenge_id
), Total_Submission_Stats AS (
    SELECT
        challenge_id,
        SUM(total_submissions) AS total_submissions,
        SUM(total_accepted_submissions) AS total_accepted_submissions
    FROM Submission_Stats
    GROUP BY challenge_id
)

SELECT
    CON.contest_id,
    CON.hacker_id,
    CON.name,
    COALESCE(SUM(TSS.total_submissions), 0) AS total_submissions,
    COALESCE(SUM(TSS.total_accepted_submissions), 0) AS total_accepted_submissions,
    COALESCE(SUM(TVS.total_views), 0) AS total_views,
    COALESCE(SUM(TVS.total_unique_views), 0) AS total_unique_views
FROM Challenges CHA
LEFT JOIN Colleges COL ON CHA.college_id = COL.college_id
LEFT JOIN Contests CON ON COL.contest_id = CON.contest_id
LEFT JOIN Total_View_Stats TVS ON CHA.challenge_id = TVS.challenge_id
LEFT JOIN Total_Submission_Stats TSS ON CHA.challenge_id = TSS.challenge_id
GROUP BY CON.contest_id, CON.hacker_id, CON.name
HAVING
    COALESCE(SUM(TSS.total_submissions), 0) +
    COALESCE(SUM(TSS.total_accepted_submissions), 0) +
    COALESCE(SUM(TVS.total_views), 0) +
    COALESCE(SUM(TVS.total_unique_views), 0) > 0
ORDER BY CON.contest_id ASC;