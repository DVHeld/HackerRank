/* https://www.hackerrank.com/challenges/weather-observation-station-2/problem */

SELECT
    CAST(SUM(LAT_N) AS DECIMAL(10,2)),
    CAST(SUM(LONG_W) AS DECIMAL(10,2))
FROM STATION;