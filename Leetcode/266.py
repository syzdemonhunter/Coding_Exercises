# https://leetcode.com/problems/palindrome-permutation/
# T: O(n)
# S: O(n)

import collections
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counts = collections.Counter(s)
        odd = 0
        
        for cnt in counts.values():
            if cnt % 2:
                odd += 1
            if odd > 1:
                return False
            
        return True