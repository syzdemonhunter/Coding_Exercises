# https://leetcode.com/problems/sort-colors/
# T: O(n)
# S: O(1)

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 0:
            return 
        cnt0 = cnt1 = cnt2 = 0
        for num in nums:
            if num == 0:
                cnt0 += 1
            elif num == 1:
                cnt1 += 1
            else:
                cnt2 += 1
                
        k = 0
        i = j = l = 0
        while i < cnt0:
            nums[k] = 0
            k += 1
            i += 1
            
        while j < cnt1:
            nums[k] = 1
            k += 1
            j += 1
            
        while l < cnt2:
            nums[k] = 2
            k += 1
            l += 1