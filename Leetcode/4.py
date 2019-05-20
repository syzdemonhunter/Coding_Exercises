# https://leetcode.com/problems/median-of-two-sorted-arrays/
# T: O(log(m + n))
# S: O(m + n)

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1, l2 = len(nums1), len(nums2)
        total = l1 + l2
        if total % 2 != 0:
            return self.helper(nums1, nums2, total / 2 + 1)
        else:
            a = self.helper(nums1, nums2, total / 2)
            b = self.helper(nums1, nums2, total / 2 + 1)
            return (float(a + b)) / 2
        
    def helper(self, nums1, nums2, k):
        # find k smallest in sorted array
        l1, l2 = len(nums1), len(nums2)
        base1, base2 = 0, 0
        while True:
            if l1 == 0:
                return nums2[k + base2 - 1]
            if l2 == 0:
                return nums1[k + base1 - 1]
            if k == 1:
                return min(nums1[base1], nums2[base2])
            
            i = min(k / 2, l1)
            j = min(k - i, l2)
            a = nums1[base1 + i - 1]
            b = nums2[base2 + j - 1]
            if i + j == k and a == b:
                return a
            if a <= b:
                base1 += i
                l1 -= i
                k -= i
            if a >= b:
                base2 += j
                l2 -= j
                k -= j
        
        