# https://leetcode.com/problems/top-k-frequent-elements/

'''
# T: O(nlogk)
# S: O(n)

import heapq
import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        dic = collections.Counter(nums)
        max_heap = [(-v, k) for k, v in dic.items()]
        heapq.heapify(max_heap)
        
        for i in range(k):
            result.append(heapq.heappop(max_heap)[1])
        return result
'''
# T: O(n)
# S: O(n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for num in counts.keys():
            buckets[counts[num]].append(num)
            
        result = []
        for i in range(len(nums), 0, -1):
            result += buckets[i]
            if len(result) == k:
                return result
            
        return result

