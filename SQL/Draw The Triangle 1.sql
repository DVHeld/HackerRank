/* https://www.hackerrank.com/challenges/draw-the-triangle-1/problem */

WITH StarAmounts AS (
    SELECT 20 AS Amount
    UNION ALL
    SELECT Amount - 1
    FROM StarAmounts
    WHERE Amount > 0
)

SELECT REPLICATE('* ', Amount) FROM StarAmounts;