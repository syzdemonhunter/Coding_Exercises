# https://leetcode.com/problems/subarray-sum-equals-k/
# https://www.youtube.com/watch?v=aYfwus5T3Bs
# T: O(n)
# S: O(n)

# prefix_sum[i] = sum of subarry(0, i) = nums[0] + .... nums[i]
# = prefix_sum[i - 1] + nums[i]
# find how many paris of (i, j) where i < j, prefix_sum[j] - prefix_sum[i] == k

# index:         0, 1, 2
# nums:          1, 1, 1
# prefix_sum: 0, 1, 2, 3
# d:         {0:1, 1:1, 2:1, 3:1}

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0
        sums = {}
        sums[0] = 1
        prefix_sum = 0
        count = 0
        for num in nums:
            prefix_sum += num
            count += sums.get(prefix_sum - k, 0)
            sums[prefix_sum] = sums.get(prefix_sum, 0) + 1
        return count
        