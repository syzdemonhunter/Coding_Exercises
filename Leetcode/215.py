# https://leetcode.com/problems/kth-largest-element-in-an-array/
# 这题非常非常重要
# 1. Quick Select
# T: O(n)
# SL O(1)

'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums or len(nums) == 0:
            return 0
        left, right = 0, len(nums) - 1
        while True:
            pos = self.partition(nums, left, right)
            if pos + 1 == k:
                return nums[pos]
            elif pos + 1 > k:
                right = pos - 1
            else:
                left = pos + 1
                
    def partition(self, nums, left, right):
        pivot = nums[left]
        l = left + 1
        r = right
        while l <= r:
            if nums[l] < pivot and nums[r] > pivot:
                self.swap(nums, l, r)
                l += 1
                r -= 1
            if nums[l] >= pivot:
                l += 1
            if nums[r] <= pivot:
                r -= 1
        self.swap(nums, left, r)
        return r
        
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
     
'''
# 2. Heap
# T: O(nlogk)
# S: O(n)

import heapq

class Solution(object):
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0
        
        min_heap = []
        
        for num in nums:
            heapq.heappush(min_heap, num) 
            
            if len(min_heap) > k:
                heapq.heappop(min_heap)
                
        return heapq.heappop(min_heap)