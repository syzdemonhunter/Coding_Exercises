# https://leetcode.com/problems/happy-number/
# T: ?
# S: O(n)

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        d = set()
        while n != 1:
            n = sum([int(i)**2 for i in str(n)])
            if n in d:
                return False
            else:
                d.add(n)
                
        return True