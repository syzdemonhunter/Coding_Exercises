# https://leetcode.com/problems/find-pivot-index/
# T: O(n)
# S: O(1)

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        total_so_far = 0
        
        for idx, num in enumerate(nums):
            if total_so_far + num == total - total_so_far:
                return idx
            
            total_so_far += num
            
        return -1
        