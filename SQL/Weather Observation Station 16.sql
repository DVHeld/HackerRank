/* https://www.hackerrank.com/challenges/weather-observation-station-16/problem */

SELECT TOP 1
    CAST(LAT_N AS DECIMAL(10, 4))
FROM STATION
WHERE LAT_N > 38.7780
ORDER BY LAT_N ASC;