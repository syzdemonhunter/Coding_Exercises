# https://leetcode.com/problems/shortest-word-distance/
# O(n) time, O(1) space

class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        size = len(words)
        idx1, idx2 = size, size
        result = size
        for i in range(size):
            if words[i] == word1:
                idx1 = i
                result = min(result, abs(idx1 - idx2))
            elif words[i] == word2:
                idx2 = i
                result = min(result, abs(idx1 - idx2))
                
        return result
        