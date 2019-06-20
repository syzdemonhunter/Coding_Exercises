# https://leetcode.com/problems/3sum-closest/
# T: O(n^2)
# S: O(1)

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        result = nums[0] + nums[1] + nums[len(nums) - 1]
        nums.sort()
        
        for i in range(len(nums)):
            start = i + 1
            end = len(nums) - 1
            while start < end:
                total = nums[i] + nums[start] + nums[end]
                if total > target:
                    end -= 1
                else:
                    start += 1
                    
                if abs(total - target) < abs(result - target):
                    result = total
                    
        return result
        
        