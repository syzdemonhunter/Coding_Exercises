# https://leetcode.com/problems/jump-game-ii/
# T: O(n)
# S: O(1)

class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums or len(nums) < 2:
            return 0
        
        result = 0
        cur_max_area = 0
        max_next = 0
        
        for i in range(len(nums) - 1):
            max_next = max(max_next, i + nums[i])
            if i == cur_max_area:
                result += 1
                cur_max_area = max_next
                
        return result