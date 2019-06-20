# https://leetcode.com/problems/3sum/
# T: O(n^2)
# S: O(n)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            low, high = i + 1, len(nums) - 1
            total = 0 - nums[i]
            while low < high:
                if nums[low] + nums[high] == total:
                    result.append([nums[i], nums[low], nums[high]])
                    while low < high and nums[low] == nums[low + 1]:
                        low += 1
                    while low < high and nums[high] == nums[high - 1]:
                        high -= 1
                    low += 1
                    high -= 1
                elif nums[low] + nums[high] < total:
                    low += 1
                else:
                    high -= 1
                    
        return result
        
        
        