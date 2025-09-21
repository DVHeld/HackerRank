/* https://www.hackerrank.com/challenges/placements/problem */

SELECT S.Name
FROM Students S
LEFT JOIN Packages SP ON S.ID = SP.ID
LEFT JOIN Friends F ON S.ID = F.ID
LEFT JOIN Packages FP ON F.Friend_ID = FP.ID
WHERE SP.Salary < FP.Salary
ORDER BY FP.Salary;