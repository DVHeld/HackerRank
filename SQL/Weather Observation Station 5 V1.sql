/* https://www.hackerrank.com/challenges/weather-observation-station-5/problem */

SELECT TOP 1 CITY, LEN(CITY) AS Length FROM STATION ORDER BY LEN(CITY) ASC, CITY ASC;
SELECT TOP 1 CITY, LEN(CITY) AS Length FROM STATION ORDER BY LEN(CITY) DESC, CITY ASC;