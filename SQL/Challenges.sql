/* https://www.hackerrank.com/challenges/challenges/problem */

WITH HackerChallenges AS (
    SELECT DISTINCT
        H.hacker_id,
        H.name,
        COUNT(*) AS Challenge_Amt
    FROM Hackers H
    LEFT JOIN Challenges C ON H.hacker_id = C.hacker_id
    GROUP BY H.hacker_id, H.name
), HackerChallengesFreqs AS (
    SELECT
        hacker_id,
        name,
        Challenge_Amt,
        MAX(Challenge_Amt) OVER () AS Max_Challenge_Amt,
        COUNT(*) OVER (PARTITION BY Challenge_Amt) AS Challenge_Amt_Freq
    FROM HackerChallenges
)
    
SELECT
    hacker_id,
    name,
    Challenge_Amt
FROM HackerChallengesFreqs
WHERE Challenge_Amt_Freq = 1 OR Challenge_Amt = Max_Challenge_Amt
ORDER BY Challenge_Amt DESC, hacker_id ASC;