# https://leetcode.com/problems/top-k-frequent-elements/
# http://zxi.mytechroad.com/blog/hashtable/leetcode-347-top-k-frequent-elements/
# Time complexity:  O(n) + O(nlogk)
# Space complexity: O(n)

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = collections.Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for num in counts.keys():
            buckets[counts[num]].append(num)
            
        ans = []
        for i in range(len(nums), 0, -1):
            ans += buckets[i]
            if len(ans) == k:
                return ans
            
        return ans