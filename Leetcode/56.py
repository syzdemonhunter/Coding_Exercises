# https://leetcode.com/problems/merge-intervals/
# T: O(log(n))
# S: O(1)


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        
        result = []
        intervals = sorted(intervals)
        
        for interval in intervals:
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])
                
        return result