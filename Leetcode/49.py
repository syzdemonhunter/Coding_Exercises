# https://leetcode.com/problems/group-anagrams/
# T: O(m*n) <- m = len(strs), n = the length of the longest string in strs
# S: O(n)

import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)
        for s in strs:
            count = [0]*26
            for ch in s:
                idx = ord(ch) - ord('a')
                count[idx] += 1
                
            dic[tuple(count)].append(s)
            
        return list(dic.values())
                
                
        