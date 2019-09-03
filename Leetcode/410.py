# https://leetcode.com/problems/split-array-largest-sum/
# T: O(nlogn)
# S: O(1)

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        max_val = 0
        total = 0
        for num in nums:
            max_val = max(num, max_val)
            total += num
            
        if m == 1:
            return total
        left = max_val
        right = total
        while left <= right:
            mid = left + (right - left)//2
            if self.valid(mid, nums, m):
                right = mid - 1
            else:
                left = mid + 1
                
        return left
                
                
    def valid(self, target, nums, m):
        count = 1
        total = 0
        for num in nums:
            total += num
            if total > target:
                total = num
                count += 1
                if count > m:
                    return False
        return True
        