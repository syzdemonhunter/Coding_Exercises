# https://leetcode.com/problems/valid-triangle-number/
# 排序后类似 3sum 进行双指针即可，时间复杂度 O(n^2)。
# T: O(n^2)
# S: O(1)

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        total = 0
        
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                continue
            end = i + 2
            for j in range(i + 1, len(nums) - 1):
                while end < len(nums) and nums[end] < (nums[i] + nums[j]):
                    end += 1
                total += end - j - 1
                
        return total
                    
        