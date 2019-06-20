# https://leetcode.com/problems/rotate-array/
# T: O(n)
# S: O(1)

'''
# T: O(n)
# S: O(n)

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tmp = [0]*len(nums)
        for i in range(len(nums)):
            tmp[(i + k) % len(nums)] = nums[i]
        for i in range(len(nums)):
            nums[i] = tmp[i]
'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)
        
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
            