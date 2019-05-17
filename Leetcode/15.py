# https://leetcode.com/problems/3sum/
# T: O(n^2)
# S: O(1)


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        nums = sorted(nums)
        result = []
        
        k = len(nums) - 1
        while k >= 2:
            if nums[k] < 0:
                break
            target = -nums[k]
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] == target:
                    result.append([nums[i], nums[j], nums[k]])
                    while i < j and nums[i] == nums[i + 1]:
                        i += 1
                    while i < j and nums[j] == nums[j - 1]:
                        j -= 1
                    i += 1
                    j -= 1
                elif nums[i] + nums[j] < target:
                    i += 1
                else:
                    j -= 1

            while k >= 2 and nums[k - 1] == nums[k]:
                k -= 1
            k -= 1
        return result