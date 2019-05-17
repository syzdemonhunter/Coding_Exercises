# https://leetcode.com/problems/majority-element/
# T: O(n)
# S: O(1)

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = nums[0]
        count = 1
        
        for i in range(1, len(nums)):
            if count == 0:
                num = nums[i]
                count = 1
            
            elif nums[i] == num:
                count += 1
            else:
                count -= 1
                
        return num