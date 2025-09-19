/* https://www.hackerrank.com/challenges/earnings-of-employees/problem */

WITH EmployeeEarnings AS (
    SELECT
        salary * months AS Total_Earnings
    FROM Employee
)

SELECT TOP 1
    Total_Earnings,
    COUNT(*)
FROM EmployeeEarnings
GROUP BY Total_Earnings
ORDER BY Total_Earnings DESC;