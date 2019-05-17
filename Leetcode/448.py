# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# T: O(n)
# S: O(1)


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        result = []
        
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
                
        for j in range(len(nums)):
            if nums[j] > 0:
                result.append(j + 1)
                
        return result
        