# https://leetcode.com/problems/ugly-number-ii/
# T: O(n)
# S: O(n)

class Solution(object):
    def min_of_three(self, a, b, c):
        return min(a, min(b, c))
    
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return -1
        results = [1]
        
        p2, p3, p5 = 0, 0, 0
        for i in range(1, n):
            min_val = self.min_of_three(results[p2]*2,
                                        results[p3]*3,
                                        results[p5]*5)
            results.append(min_val)
            if min_val == results[p2]*2:
                p2 += 1
            if min_val == results[p3]*3:
                p3 += 1
            if min_val == results[p5]*5:
                p5 += 1
                
        return results[n - 1]
            