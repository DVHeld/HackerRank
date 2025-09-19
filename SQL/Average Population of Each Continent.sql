/* https://www.hackerrank.com/challenges/average-population-of-each-continent/problem */

SELECT
    CO.CONTINENT,
    CAST(AVG(CI.POPULATION) AS DECIMAL(10,0))
FROM CITY CI
INNER JOIN COUNTRY CO ON CI.COUNTRYCODE = CO.CODE
GROUP BY CO.CONTINENT;