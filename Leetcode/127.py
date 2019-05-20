# https://leetcode.com/problems/word-ladder/
# T: O(word_len*size of word_list)
# S: O(size of word_list)

from collections import defaultdict, deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList: 
            return 0

        graph = defaultdict(list)
        length = len(beginWord)
        for word in wordList:
            for i in range(length):
                s = word[:i]+'_'+word[i+1:]
                graph[s].append(word)
            
        q = deque([beginWord])
        visited = set()
        distance = 1
        while q:
            newq = []
            while q:
                cur = q.popleft()
                visited.add(cur)
                if cur == endWord:
                    return distance
                for i in range(length):
                    s = cur[:i]+'_'+cur[i+1:]
                    for inner_word in graph[s]:
                        if inner_word in visited: 
                            continue
                        visited.add(inner_word)
                        newq.append(inner_word)                          
            q.extend(newq)
            distance += 1      
        return 0