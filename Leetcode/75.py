# https://algocasts.io/episodes/aVWyAYW2
# T: O(n)
# S: O(1)

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
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
            

#### or #####
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 0:
            return 
        
        left = mid = 0
        right = len(nums) - 1
        while mid <= right:
            if nums[mid] == 0:
                nums[mid], nums[left] = nums[left], nums[mid]
                mid += 1
                left += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[right], nums[mid] = nums[mid], nums[right]
                right -= 1