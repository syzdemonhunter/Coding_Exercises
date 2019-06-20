# https://leetcode.com/problems/jump-game/
# T: O(n)
# S: O(1)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_val = 0
        for i in range(len(nums)):
            if i > max_val:
                return False
            max_val = max(nums[i] + i, max_val)
            
        return True