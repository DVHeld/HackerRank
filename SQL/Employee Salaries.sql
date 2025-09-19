/* https://www.hackerrank.com/challenges/salary-of-employees/problem */

SELECT name
FROM Employee
WHERE salary > 2000 AND
      months < 10;