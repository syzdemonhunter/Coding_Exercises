# https://leetcode.com/problems/strobogrammatic-number/
# T: O(n)
# S: O(1)

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        if not num: 
            return False
        
        pairs = set([('0','0'), ('1','1'), ('6','9'), ('8','8'), ('9','6')])
        l, r = 0, len(num) - 1
        
        while l <= r:
            if (num[l], num[r]) not in pairs:
                return False
            l += 1
            r -= 1
        return True

        