# https://leetcode.com/problems/find-the-celebrity/
# T: O(n)
# S: O(1)

# https://www.youtube.com/watch?v=LZJBZEnoYLQ
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
        candidate = 0
        
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i
                
        for i in range(n):
            if i != candidate and \
            knows(candidate, i) or \
            not knows(i, candidate):
                return -1
            
        return candidate