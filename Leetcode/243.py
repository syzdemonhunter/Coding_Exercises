# https://leetcode.com/problems/shortest-word-distance/

'''
# T: O(n^2)
# S: O(1)
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        result = len(words)
        for i in range(len(words)):
            if words[i] == word1:
                for j in range(len(words)):
                    if words[j] == word2:
                        result = min(result, abs(i - j))
            
        return result
'''
# T: O(n)
# S: O(1)
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        result = len(words)
        a = -1
        b = -1
        for i in range(len(words)):
            if words[i] == word1:
                a = i
            elif words[i] == word2:
                b = i
            if a != -1 and b != -1:
                result = min(result, abs(a - b))            
        return result