# https://leetcode.com/problems/circular-array-loop/
# T: O(n)
# S: O(1)

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        for i, num in enumerate(nums):
            # use a distinct marker for each starting point
            mark = str(i)
            
            # explore while node is new, direction is same, and is not self loop
            # note: if node has been marked by a different marker, no need to proceed. This gives O(n) time.
            while (type(nums[i]) == int) and (num * nums[i] > 0) and (nums[i] % len(nums) != 0):
                jump = nums[i] 
                nums[i] = mark
                i = (i + jump) % len(nums)
            
            # if self loop, nums[i] is never marked
            # if nums[i] is marked, a cycle is found
            if nums[i] == mark:
                return True
            
        return False