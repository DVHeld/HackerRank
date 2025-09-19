/* https://www.hackerrank.com/challenges/asian-population/problem */

SELECT SUM(CI.POPULATION)
FROM CITY CI
LEFT JOIN COUNTRY CO ON CI.CountryCode = CO.Code
WHERE CO.CONTINENT = "Asia";