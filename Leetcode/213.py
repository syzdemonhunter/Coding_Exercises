# https://leetcode.com/problems/house-robber-ii/
# T: O(n)
# S: O(1)

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_helper(nums, 0, len(nums) - 2),\
                   self.rob_helper(nums, 1, len(nums) - 1))
                   
    def rob_helper(self, nums, start, end):
        pre1, pre2 = 0, 0
        for i in range(start, end + 1):
            cur = max(pre1, pre2 + nums[i])
            pre2 = pre1
            pre1 = cur
        return pre1