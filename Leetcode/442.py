# https://leetcode.com/problems/find-all-duplicates-in-an-array/
# 我们发现对数组的所有元素均有1\leq a[i]\leq n1≤a[i]≤n，也就是说对于所有a[a[i]-1]均为合法下标。由此引出如下做法：
# 对于每个a[i]，我们将其对应的a[a[i]-1]取相反数，如果已经为负数则将a[i]加入答案中。

# T: O(n)
# S: O(n)

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        result = []
        for i in range(len(nums)):
            idx = nums[i]
            if idx < 0:
                idx = -idx
            if nums[idx - 1] > 0:
                nums[idx - 1] = -nums[idx - 1]
            else:
                result.append(idx)
        return result
        