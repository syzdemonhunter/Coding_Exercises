# https://leetcode.com/problems/word-ladder/
# T: O(n)
# S: O(n)

import collections

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: 
            return 0

        graph = collections.defaultdict(list)
        length = len(beginWord)
        for word in wordList:
            for i in range(length):
                s = word[:i] + '_' + word[i+1:]
                graph[s].append(word)
            
        q = collections.deque([beginWord])
        visited = set()
        distance = 1
        while q:
            tmp = []
            while q:
                cur = q.popleft()
                visited.add(cur)
                if cur == endWord:
                    return distance
                for i in range(length):
                    s = cur[:i] + '_' + cur[i+1:]
                    for inner_word in graph[s]:
                        if inner_word in visited: 
                            continue
                        visited.add(inner_word)
                        tmp.append(inner_word)                          
            q.extend(tmp)
            distance += 1      
        return 0
        
        
        
        
        
        