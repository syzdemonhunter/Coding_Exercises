# https://leetcode.com/problems/wiggle-sort-ii/
# O(nlogn) 的时间，O(1) 额外空间

# 这个问题的做法是，先找到中位数，然后根据中位数把数组分成三个部分，< median, == median, > median
# 然后把这三个部分按照从大到小摆放在从右到左每次跳一格的位置。


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        
        nums.sort()
        half = len(nums[::2]) - 1
        nums[::2], nums[1::2] = nums[half::-1], nums[:half:-1]