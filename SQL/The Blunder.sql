/* https://www.hackerrank.com/challenges/the-blunder/problem */

SELECT
    CAST(
        CEILING(AVG(CAST(SALARY AS FLOAT)) -
        AVG(CAST(REPLACE(CAST(SALARY AS VARCHAR), "0", "") AS FLOAT)))
        AS INT)
FROM EMPLOYEES;