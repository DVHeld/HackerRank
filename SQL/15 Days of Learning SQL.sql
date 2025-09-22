/* https://www.hackerrank.com/challenges/15-days-of-learning-sql/problem */

WITH SubmissionsByHackerDay AS (
    SELECT
        submission_date,
        hacker_id,
        COUNT(*) AS submission_amt
    FROM Submissions
    GROUP BY submission_date, hacker_id
), SubmissionsWithRankings AS (
    SELECT
        submission_date,
        hacker_id,
        submission_amt,
        COUNT(*) OVER (PARTITION BY hacker_id ORDER BY submission_date) AS days_submitted, 
        ROW_NUMBER() OVER (PARTITION BY submission_date ORDER BY submission_amt DESC, hacker_id ASC) AS ranking
    FROM SubmissionsByHackerDay
), StartDate AS (
    SELECT MIN(submission_date) AS start_date
    FROM Submissions
), HasSubmittedDaily AS (
    SELECT
        S.submission_date,
        S.hacker_id,
        CASE
            WHEN S.days_submitted = DATEDIFF(DAY, D.start_date, S.submission_date)+1 THEN 1
            ELSE 0
        END AS has_submitted_daily
    FROM SubmissionsWithRankings S
    CROSS JOIN StartDate D
    GROUP BY S.submission_date, S.hacker_id, S.days_submitted, D.start_date
), DalySubmissions AS (
    SELECT
        submission_date,
        SUM(has_submitted_daily) AS hacker_amt
    FROM HasSubmittedDaily
    GROUP BY submission_date    
)

SELECT
    S.submission_date,
    D.hacker_amt,
    S.hacker_id,
    H.name
FROM SubmissionsWithRankings S
LEFT JOIN Hackers H ON S.hacker_id = H.hacker_id
LEFT JOIN DalySubmissions D ON S.submission_date = D.submission_date
WHERE S.ranking = 1
ORDER BY S.submission_date ASC;