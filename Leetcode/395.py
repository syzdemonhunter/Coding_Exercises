# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
# T: O(n)
# S: O(n)

# 对于一个字符串，若其中某一个字符的数量小于k，则最终的答案中一定不会包含这个字符，因此答案只有可能在这个字符的左右两侧的字符串。
# 之后对于左右两边的串递归处理即可。
import collections

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        lookup = collections.Counter(s)
        for c in lookup:
            if lookup[c] < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)
        