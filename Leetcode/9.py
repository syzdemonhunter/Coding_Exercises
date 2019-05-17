# https://leetcode.com/problems/palindrome-number/
# T: O(m)
# S: O(1)


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        tmp = x
        y = 0
        while tmp != 0:
            num = tmp % 10
            y = y*10 + num
            tmp = tmp//10
        return x == y