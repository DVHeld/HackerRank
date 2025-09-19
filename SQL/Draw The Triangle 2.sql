/* https://www.hackerrank.com/challenges/draw-the-triangle-2/problem */

WITH StarAmounts AS (
    SELECT 1 AS Amount
    UNION ALL
    SELECT Amount + 1
    FROM StarAmounts
    WHERE Amount < 20
)

SELECT REPLICATE('* ', Amount) FROM StarAmounts;