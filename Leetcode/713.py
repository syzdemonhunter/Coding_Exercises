# https://leetcode.com/problems/subarray-product-less-than-k/
# 维护一个滑动窗口，left为窗口的左端点，i用来探索下一个数，left和i组成的滑动窗口为[left, i]
# 如果当前窗口中的所有数的乘积 >= k， 说明窗口不再满足条件( < k), 则把left指向的左端点的数从窗口中去掉，反映在窗口乘积上应该是除以要删除的这个数，然后left++，一直重复下去直到窗口再次满足条件，则又找到了一个新的窗口，窗口的长度就是当前窗口中满足条件的子数组个数，
# 窗口长度用 i - left + 1来表示。
# 时间复杂度为O(n)

class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prod, i, result = 1, 0, 0
        
        for j, num in enumerate(nums):
            prod *= num
            
            while i <= j and prod >= k:
                prod //= nums[i]
                i += 1
                
            result += j - i + 1
        return result