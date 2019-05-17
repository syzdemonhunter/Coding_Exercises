# https://leetcode.com/problems/top-k-frequent-words/
#T: O(n log k) time and 
#S: O(n) extra space.

import collections,heapq 

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        result, hp = [], []
        count = collections.Counter(words)
        
        for w, c in count.items():
            heapq.heappush(hp, (-c, w))
            
        for _ in range(k):
            c, w = heapq.heappop(hp)
            result.append(w)
            
        return result
        