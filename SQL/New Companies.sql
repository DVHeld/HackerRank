/* https://www.hackerrank.com/challenges/the-company/problem */

SELECT DISTINCT
    COM.company_code,
    MAX(COM.founder) AS founder,
    COUNT(DISTINCT LM.lead_manager_code) AS LeadManagerAmt,
    COUNT(DISTINCT SM.senior_manager_code) AS SeniorManagerAmt,
    COUNT(DISTINCT M.manager_code) AS ManagerAmt,
    COUNT(DISTINCT E.employee_code) AS EmployeeAmt
FROM Company COM
LEFT JOIN Lead_Manager LM ON COM.company_code = LM.company_code
LEFT JOIN Senior_Manager SM ON COM.company_code = SM.company_code
LEFT JOIN Manager M ON M.company_code = COM.company_code
LEFT JOIN Employee E ON COM.company_code = E.company_code
GROUP BY COM.company_code
ORDER BY COM.company_code ASC;