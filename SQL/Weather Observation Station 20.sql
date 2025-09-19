/* https://www.hackerrank.com/challenges/weather-observation-station-20/problem */

DECLARE @MedianRow INT = (SELECT CEILING(CAST(COUNT(*) AS FLOAT)/2) FROM STATION);

WITH LatsWithRowNo AS (
    SELECT
        LAT_N,
        ROW_NUMBER() OVER (ORDER BY LAT_N ASC) AS Row_Num
    FROM STATION
)

SELECT CAST(LAT_N AS DECIMAL(10, 4))
FROM LatsWithRowNo
WHERE Row_Num = @MedianRow;