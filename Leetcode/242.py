# https://leetcode.com/problems/valid-anagram/
# T: O(n)
# S: O(n)

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def letter_count(word):
            d = {}
            for x in word:
                d[x] = d.get(x, 0) + 1
            return d
                
        return letter_count(s) == letter_count(t)
        