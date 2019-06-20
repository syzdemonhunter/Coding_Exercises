# https://leetcode.com/problems/remove-element/
# T: O(n)
# S: O(1)

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums or len(nums) == 0:
            return 0
        
        result = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[result] = nums[i]
                result += 1
                
        return result
        