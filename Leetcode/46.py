# https://leetcode.com/problems/permutations/
# T: O(n*n!)
# S: O(n)

class Solution(object):
    def helper(self, nums, start, result):
        if start == len(nums):
            result.append(nums[:])
        else:
            for i in range(start, len(nums)):
                nums[i], nums[start] = nums[start], nums[i]
                self.helper(nums, start + 1, result)
                nums[i], nums[start] = nums[start], nums[i]
            
            
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        result = []
        work = nums[:]
        self.helper(work, 0, result)
        return result