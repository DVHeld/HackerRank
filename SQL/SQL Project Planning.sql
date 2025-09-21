/* https://www.hackerrank.com/challenges/sql-projects/problem */

WITH Project_Starts AS (
    SELECT
        Start_Date,
        End_Date,
        CASE
            WHEN Lag(End_Date) OVER (ORDER BY Start_Date) = Start_Date THEN 0
            ELSE 1
        END AS Proj_Start
    FROM Projects
), Projects_IDs AS (
    SELECT
        Start_Date,
        End_Date,
        SUM(Proj_Start) OVER (ORDER BY Start_Date) AS Proj_ID
    FROM Project_Starts
)

SELECT
    MIN(Start_Date) AS Start_Date,
    MAX(End_Date) AS End_Date
FROM Projects_IDs
GROUP BY Proj_ID
ORDER BY COUNT(*) ASC, MIN(Start_Date) ASC;