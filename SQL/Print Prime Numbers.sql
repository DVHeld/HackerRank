/* https://www.hackerrank.com/challenges/print-prime-numbers/problem */

DECLARE @N INT = 1000;

WITH NumberGenerator AS (
    SELECT 2 AS Number
    UNION ALL
    SELECT Number + 1 AS Number
    FROM NumberGenerator
    WHERE Number < @N
),

CheckPrimes AS (
    SELECT
        N1.Number AS Number,
        CASE
            WHEN EXISTS (
                SELECT 1
                FROM NumberGenerator N2
                WHERE N2.Number > 1 AND
                      N2.nUMBER < N1.Number AND
                      N1.Number % N2.Number = 0 
            ) THEN 0
            ELSE 1
        END AS Is_Prime
    FROM NumberGenerator N1
)

SELECT STRING_AGG(CAST(Number AS VARCHAR), '&')
FROM CheckPrimes
WHERE Is_Prime = 1

OPTION (MAXRECURSION 1000);