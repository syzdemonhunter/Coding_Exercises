# https://leetcode.com/problems/find-the-celebrity/
# T: O(n)
# S: O(1)

# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return -1
        possible = 0
        for i in range(1, n):
            if knows(possible, i):
                possible = i
        for i in range(n):
            if possible != i and (knows(possible, i) or not knows(i, possible)):
                return -1
        return possible
                