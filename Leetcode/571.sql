# https://leetcode.com/problems/find-median-given-frequency-of-numbers/

#suppose number x has frequency of n, and total frequency of other numbers that are on its left is l, on its right is r.
#the equation above is (n+l) - (n+r) = l - r, x is median if l==r, of course.
#When l != r, as long as n can cover the difference, x is the median.

SELECT
    AVG(n.Number) AS median
FROM
    Numbers n
WHERE 
    n.Frequency >= abs((SELECT SUM(Frequency) FROM Numbers WHERE Number<=n.Number) -
                         (SELECT SUM(Frequency) FROM Numbers WHERE Number>=n.Number))
;
