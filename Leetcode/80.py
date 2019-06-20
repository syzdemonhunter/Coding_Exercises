# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
# T: O(n)
# S: O(1)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        count = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[count - 2]:
                nums[count] = nums[i]
                count += 1
                
        return count