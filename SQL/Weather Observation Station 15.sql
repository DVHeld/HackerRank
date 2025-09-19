/* https://www.hackerrank.com/challenges/weather-observation-station-15/problem */

SELECT TOP 1
    CAST(LONG_W AS DECIMAL(10, 4))
FROM STATION
WHERE LAT_N < 137.2345
ORDER BY LAT_N DESC;