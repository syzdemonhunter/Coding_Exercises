# https://leetcode.com/problems/longest-consecutive-sequence/
# T: O(n)
# S: O(n)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        
        result = 0
        my_set = set(nums)

        for i in range(len(nums)):
            down = nums[i] - 1
            while down in my_set:
                my_set.remove(down)
                down -= 1
            up = nums[i] + 1
            while up in my_set:
                my_set.remove(up)
                up += 1
            result = max(result, up - down - 1)
            
        return result