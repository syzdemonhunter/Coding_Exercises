# https://leetcode.com/problems/reverse-words-in-a-string/
# T: O(n)
# S: O(n)

class Solution:
    def reverseWords(self, s: str) -> str:
        result = ''
        words = s.strip().split()
        for i in range(len(words) - 1, -1, -1):
            result += words[i] + ' '
        return result.strip()
        