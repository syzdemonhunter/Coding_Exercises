# https://leetcode.com/problems/nested-list-weight-sum-ii/
# T: O(n)
# S: O(n)

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
import collections

class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        if not nestedList or len(nestedList) == 0:
            return 0
        
        res = []
        q = collections.deque()
        for ele in nestedList:
            q.append(ele)
            
        while q:
            level_sum = 0
            for i in range(len(q)):
                item = q.popleft()
                
                if item.isInteger():
                    level_sum += item.getInteger()
                else:
                    for ele in item.getList():
                        q.append(ele)
                        
            res.append(level_sum)
            
        total_sum = 0
        for i in range(len(res) - 1, -1, -1):
            weight = len(res) - i
            total_sum += res[i]*weight
        return total_sum
                
        
        
        
        
        