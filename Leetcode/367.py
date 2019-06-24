'''
# T: O(n)
# S: O(1)
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 0:
            return False
        if num == 1:
            return True
        
        i = 1
        while i*i < num + 1:
            i += 1
            if i*i == num:
                return True
        
        return False
'''
'''
# T: O(logn)
# S: O(1)
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low, high = 1, num
        while low <= high:
            mid = low + (high - low)//2
            if mid*mid == num:
                return True
            elif mid*mid < num:
                low = mid + 1
            else:
                high = mid - 1
                
        return False
'''
'''
# T: O(n)
# S: O(1)
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while num > 0:
            num -= i
            i += 2
            
        return num == 0
'''
# T: 不知道
# S: O(1)
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x = num
        while x*x > num:
            x = (x + num//x)//2
            
        return x*x == num
        
        