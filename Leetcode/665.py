# https://leetcode.com/problems/non-decreasing-array/
# T: O(n)
# S: O(1)

# 从头开始模拟，碰到第一次nums[i]<nums[i-1]时，我们需要修改nums[i]或者nums[i-1]来保证数组的不下降。
# 有两种情况：
#1、nums[i]<nums[i-2]，比如3,4,2这样的情况，当前nums[i]=2。此时我们只能将nums[i]修改为4，才能在满足题意的条件下保证数组不下降，修改后为3,4,4。
# 2、nums[i]>=nums[i-2]，比如3,5,4，当前nums[i]=4。此时我们可以将nums[i-1]修改为4，修改后为3,4,4。

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                count += 1
                if i >= 2 and nums[i] < nums[i - 2]:
                    nums[i] = nums[i - 1]
                else:
                    nums[i - 1] = nums[i]
                    
        return count <= 1
        
        