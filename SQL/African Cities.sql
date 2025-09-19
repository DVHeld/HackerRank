/* https://www.hackerrank.com/challenges/african-cities/problem */

SELECT CI.NAME
FROM CITY CI
LEFT JOIN COUNTRY CO ON CI.COUNTRYCODE = CO.CODE
WHERE CO.CONTINENT = "Africa";