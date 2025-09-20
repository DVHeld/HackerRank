/* https://www.hackerrank.com/challenges/full-score/problem */

SELECT
    S.hacker_id,
    H.name
FROM Submissions S
LEFT JOIN Hackers H ON S.hacker_id = H.hacker_id
LEFT JOIN Challenges C ON S.challenge_id = C.challenge_id
LEFT JOIN Difficulty D ON C.difficulty_level = D.difficulty_level
WHERE S.score = D.score
GROUP BY S.hacker_id, H.name
HAVING COUNT(*) > 1
ORDER BY COUNT(*) DESC, hacker_id ASC;