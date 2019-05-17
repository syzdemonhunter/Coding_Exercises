# https://www.jiuzhang.com/solution/428-pow-x-n/#tag-other-lang-python
# https://leetcode.com/problems/powx-n/

#Time Complexity: O(log N)
#Space Complexity: O(1); for recurrsion, space is O(log N)
#Algorithm: Fast Power:
#* if n is even, x^n = (x ^ (n/2)) ^2;
#* if n is odd, x^n = x ^(n-1) * n

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1/x
            n = -n
            
        ans = 1
        current_prod = x
        
        while n > 0:
            if n % 2 == 1:
                ans *= current_prod
                n -= 1
            else:
                current_prod = current_prod * current_prod
                n //= 2
                
        return ans