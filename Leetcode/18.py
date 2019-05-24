# https://leetcode.com/problems/4sum/
# https://www.youtube.com/watch?v=YkxsyPItHeM
# T: O(n^3)
# S: O(n)

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        
        result = []
        nums.sort()
        
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                low, high = j + 1, len(nums) - 1
                while low < high:
                    total = nums[i] + nums[j] + nums[low] + nums[high]
                    if total == target:
                        result.append([nums[i], nums[j], nums[low], nums[high]])
                        while low < high and nums[low] == nums[low + 1]:
                            low += 1
                        while low < high and nums[high] == nums[high - 1]:
                            high -= 1
                        
                        low += 1
                        high -= 1
                    elif total < target:
                        low += 1
                    else:
                        high -= 1
                        
        return result
        