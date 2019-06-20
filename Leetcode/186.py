# https://leetcode.com/problems/reverse-words-in-a-string-ii/
# T: O(n)
# S: O(1)

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.reverse(s, 0, len(s) - 1)
        r = 0
        while r < len(s):
            l = r
            while r < len(s) and s[r] != ' ':
                r += 1
            self.reverse(s, l, r - 1)
            r += 1
            
    def reverse(self, s, i, j):
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        