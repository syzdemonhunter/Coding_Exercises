# https://leetcode.com/problems/sliding-window-maximum/
# dq: 存的是index，从大到小排序
# T: O(n)
# S: O(n)

import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or len(nums) == 0:
            return []
        
        dq = collections.deque([])
        result = [0]*(len(nums) + 1 - k)
        for i in range(len(nums)):
            if dq and dq[0] == i - k: 
                dq.popleft()
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            if i + 1 >= k:
                result[i + 1 - k] = nums[dq[0]]
                
        return result
        