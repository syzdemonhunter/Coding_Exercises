# https://leetcode.com/problems/find-the-duplicate-number/
'''
# T: O(nlogn)
# S: O(1)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        min_val = 0
        max_val = len(nums) - 1
        while min_val <= max_val:
            mid = min_val + (max_val - min_val)//2
            count = 0
            for i in range(len(nums)):
                if nums[i] <= mid:
                    count += 1
            if count > mid:
                max_val = mid - 1
            else:
                min_val = mid + 1
                
        return min_val
'''
# T: O(n)
# S: O(1)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
        
