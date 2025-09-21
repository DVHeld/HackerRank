/* https://www.hackerrank.com/challenges/contest-leaderboard/problem */

SELECT
    H.hacker_id,
    H.name,
    SUM(challenge_score) as total_score
FROM Hackers H
INNER JOIN (
    SELECT
        hacker_id,
        MAX(score) AS challenge_score
    FROM Submissions
    GROUP BY hacker_id, challenge_id
) MS ON H.hacker_id = MS.hacker_id
GROUP BY H.hacker_id, H.name
HAVING SUM(challenge_score) > 0
ORDER BY SUM(challenge_score) DESC, hacker_id ASC;