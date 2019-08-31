# T: O(n^2)
# S: O(1)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        cur_longest = [0, 1]
        for i in range(1, len(s)):
            odd = self.helper(s, i - 1, i + 1)
            even = self.helper(s, i - 1, i)
            longest = max(odd, even, key = lambda x: x[1] - x[0])
            cur_longest = max(longest, cur_longest, key = lambda x: x[1]  - x[0])
            
        return s[cur_longest[0]:cur_longest[1]]
            
    def helper(self, s, left, right):
        while left >= 0  and right < len(s):
            if s[left] != s[right]:
                break
            left -= 1
            right += 1

        return [left + 1, right]
