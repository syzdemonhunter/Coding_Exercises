# https://leetcode.com/problems/group-anagrams/
# T: O(n*k*log(k))
# S: O(n)

import collections

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = collections.defaultdict(list)
        for s in strs:
            d[''.join(sorted(s))].append(s)
            
        return [g for g in d.values()]