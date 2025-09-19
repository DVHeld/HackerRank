/* https://www.hackerrank.com/challenges/occupations/problem */

SELECT [Doctor], [Professor], [Singer], [Actor]
FROM (
    SELECT
        Name,
        Occupation,
        ROW_NUMBER() OVER (PARTITION BY Occupation ORDER BY Name) AS Row_Num
    FROM OCCUPATIONS
) AS OccupationsWithRowNum
PIVOT (
    MAX(Name) FOR Occupation IN ([Doctor], [Professor], [Singer], [Actor])
) AS PivotedOccupations
ORDER BY Row_Num;