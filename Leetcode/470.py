# https://leetcode.com/problems/implement-rand10-using-rand7/

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        x = 2**32
        # 1-49 with equal probability
        while x > 40:
            x = 7*(rand7() - 1) + rand7()
        return x%10 + 1