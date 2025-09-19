/* https://www.hackerrank.com/challenges/binary-search-tree-1/problem */

SELECT
    A.N,
    CASE
        WHEN A.P IS NULL THEN 'Root'
        WHEN A.N IN (SELECT DISTINCT B.P FROM BST B) THEN 'Inner'
        ELSE 'Leaf'
    END
FROM BST A
ORDER BY A.N;