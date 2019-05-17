# https://leetcode.com/problems/subsets/
# T: O(n*2^n)
# S: O(n)

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        
        def dfs(n, start, cur):
            if n == len(cur):
                result.append(cur[:])
                return
            
            for i in range(start, len(nums)):
                cur.append(nums[i])
                dfs(n, i + 1, cur)
                cur.pop()
                
        for j in range(len(nums) + 1):
            dfs(j, 0, [])
            
        return result
        