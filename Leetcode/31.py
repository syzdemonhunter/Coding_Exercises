# https://leetcode.com/problems/next-permutation/
# T: O(n)
# S: O(1)

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 0:
            return
        
        p = len(nums) - 2
        while p >= 0 and nums[p] >= nums[p + 1]:
            p -= 1
            
        if p == -1:
            nums.reverse()
            return
        
        for i in reversed(range(p + 1, len(nums))):
            if nums[i] > nums[p]:
                nums[p], nums[i] = nums[i], nums[p]
                break
                
        nums[p + 1:] = reversed(nums[p + 1:])
            