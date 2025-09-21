/* https://www.hackerrank.com/challenges/symmetric-pairs/problem */

WITH FunctionsWithID AS (
    SELECT
        X,
        Y,
        ROW_NUMBER() OVER (ORDER BY X ASC) AS ID
    FROM Functions
)

SELECT DISTINCT A.X, A.Y
FROM FunctionsWithID A
INNER JOIN FunctionsWithID B ON A.X = B.Y AND A.Y = B.X AND A.ID <> B.ID
WHERE A.X <= A.Y
ORDER BY A.X;