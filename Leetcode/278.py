# https://leetcode.com/problems/first-bad-version/submissions/
# T: O(log(n))
# S: O(1)


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 1, n
        while start <= end:
            mid = start + (end - start) // 2
            if isBadVersion(mid):
                end = mid - 1
            else:
                start = mid + 1
        
        if isBadVersion(start):
            return start
        else:
            return end