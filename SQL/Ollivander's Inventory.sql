/* https://www.hackerrank.com/challenges/harry-potter-and-wands/problem */

WITH NumberedWands AS (
    SELECT
        W.id,
        P.age,
        W.coins_needed,
        W.power,
        ROW_NUMBER() OVER (PARTITION BY P.age, W.power ORDER BY W.coins_needed ASC) AS RowNum
    FROM Wands W
    LEFT JOIN Wands_Property P ON W.code = P.code
    WHERE P.is_evil = 0
)

SELECT 
    id,
    age,
    coins_needed,
    power
FROM NumberedWands
WHERE RowNum = 1
ORDER BY power DESC, age DESC;