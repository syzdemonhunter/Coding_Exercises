# https://leetcode.com/problems/shortest-word-distance-iii/
# T: O(n)
# S: O(1)

class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        result = len(words)
        a, b = -1, -1
        for i in range(len(words)):
            if words[i] == word1:
                a = i 
            if words[i] == word2:
                if word1 == word2:
                    a = b
                b = i
            if a != -1 and b != -1:
                result = min(result, abs(a - b))
                
        return result
        