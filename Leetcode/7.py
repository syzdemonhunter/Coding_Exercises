# https://leetcode.com/problems/reverse-integer/
# T: O(n)
# S: O(1)

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result, remain = 0, abs(x)
        while remain:
            result = result * 10 + remain % 10
            remain = remain // 10
            
        if x < 0:
            ans = int(result) * -1
        else:
            ans = int(result)
        
        if not (-1*2**31 <= ans <= 2**31-1):
            return 0
        else:
            return ans

            