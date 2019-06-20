# https://leetcode.com/problems/sqrtx/
# T: O(logn)
# S: O(1)

class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 0:
            return 0
        
        low, high = 1, x
        while low <= high:
            mid = low + (high - low)//2
            if mid*mid == x:
                return mid
            elif mid*mid < x:
                low = mid + 1
            else:
                high = mid - 1
                
        if high*high < x:
            return high
        else:
            return low