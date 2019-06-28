# https://leetcode.com/problems/russian-doll-envelopes/
# T: O(nlogn)
# S: O(n)

class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes or len(envelopes) == 0:
            return 0
        
        tails = []
        for _, h in sorted(envelopes, key = lambda env : (env[0], -env[1])):
            pos = bisect.bisect_left(tails, h)
            if pos == len(tails):
                tails.append(h)
            else:
                tails[pos] = h
        return len(tails)      