# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# T: O(n)
# S: O(1)

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            n = abs(nums[i])
            nums[n - 1] = -abs(nums[n - 1])
            
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)
        return result