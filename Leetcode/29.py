# https://leetcode.com/problems/divide-two-integers/
# https://www.youtube.com/watch?v=2bNV08KroqQ
# time: O(log(n)*log(n))
# space: O(log(n))

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1
        if ((dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0)):
            sign = -1
            
        dividend_abs = abs(dividend)
        divisor_abs = abs(divisor)
        if dividend_abs <  divisor_abs or  dividend_abs == 0:
            return 0
        
        res_abs = self.helper(dividend_abs, divisor_abs)
        return min(max(-2**31, res_abs*sign), 2**31 -1)
        
    def helper(self, dividend_abs, divisor_abs):
        if dividend_abs < divisor_abs:
            return 0
        
        total = divisor_abs
        multiple = 1
        while total + total < dividend_abs:
            total += total
            multiple += multiple
            
        return multiple + self.helper(dividend_abs - total, divisor_abs)
        
            
        