# https://leetcode.com/problems/ugly-number-ii/
# T: O(n)
# S: O(n)

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [0]*n
        idx_2, idx_3, idx_5 = 0, 0, 0
        nums[0] = 1
        for i in range(1, len(nums)):
            nums[i] = min(nums[idx_2]*2, min(nums[idx_3]*3, nums[idx_5]*5))
            if nums[i] == nums[idx_2]*2:
                idx_2 += 1
            if nums[i] == nums[idx_3]*3:
                idx_3 += 1
            if nums[i] == nums[idx_5]*5:
                idx_5 += 1
                
        return nums[n - 1]