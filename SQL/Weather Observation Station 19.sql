/* https://www.hackerrank.com/challenges/weather-observation-station-19/problem */

DECLARE @X1 FLOAT = (SELECT MIN(LAT_N) FROM STATION);
DECLARE @X2 FLOAT = (SELECT MAX(LAT_N) FROM STATION);
DECLARE @Y1 FLOAT = (SELECT MIN(LONG_W) FROM STATION);
DECLARE @Y2 FLOAT = (SELECT MAX(LONG_W) FROM STATION);

SELECT
    CAST(SQRT(
        POWER(@X2 - @X1, 2) +
        POWER(@Y2 - @Y1, 2)
    ) AS DECIMAL(10, 4));