# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# T: O(n)
# S: O(1)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j - 1] != nums[j]:
                i += 1
                nums[i] = nums[j]
                
        return i + 1
        