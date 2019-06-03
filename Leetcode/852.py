# https://leetcode.com/problems/peak-index-in-a-mountain-array/
# T: O(logn)
# S: O(1)

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        l, r = 0, len(A) - 1
        while True:
            idx = l + (r - l)//2
            if A[idx - 1] < A[idx] > A[idx + 1]:
                return idx
            elif A[idx - 1] < A[idx] < A[idx + 1]:
                l = idx + 1
            else:
                r = idx - 1
                
        