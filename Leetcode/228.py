# https://leetcode.com/problems/summary-ranges/
# T: O(n)
# S: O(n)

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums or len(nums) == 0:
            return []
        
        result = []
        start, end = nums[0], nums[0]
        for i in range(1, len(nums) + 1):
            if i < len(nums) and nums[i] == end + 1:
                end = nums[i]
            else:
                interval = str(start)
                if start != end:
                    interval += '->' + str(end)
                result.append(interval)
                if i < len(nums):
                    start = end = nums[i]
                    
        return result