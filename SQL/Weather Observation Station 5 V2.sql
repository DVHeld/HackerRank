/* https://www.hackerrank.com/challenges/weather-observation-station-5/problem */

SELECT TOP 2
    MIN(S.CITY) AS CITY,
    LEN(S.CITY) AS NAME_LEN
FROM STATION S
INNER JOIN (
    SELECT
        MIN(LEN(CITY)) AS MIN_LEN,
        MAX(LEN(CITY)) AS MAX_LEN
    FROM STATION
) L
ON
    LEN(S.CITY) = MIN_LEN OR
    LEN(S.CITY) = MAX_LEN
GROUP BY LEN(S.CITY)
ORDER BY LEN(S.CITY) ASC;