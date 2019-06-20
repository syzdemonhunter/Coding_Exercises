# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# T: O(n)
# S: O(1)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        count = 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[count] = nums[i]
                count += 1
            
        return count
        