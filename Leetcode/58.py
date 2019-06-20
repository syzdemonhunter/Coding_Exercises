# https://leetcode.com/problems/length-of-last-word/
# T: O(n)
# S: O(n)

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        strings = s.split()
        if len(strings) == 0:
            return 0
        return len(strings[len(strings) - 1])
        