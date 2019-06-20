# https://leetcode.com/problems/shortest-word-distance-ii/
# 因为题干中写了，会调用shortest函数非常多次，所以使用HashMap来存储words，key为word，value为index组成的list。
# 计算shortest word distance的时候，使用双指针遍历一遍即可。

# 时间复杂度
# 存储：O(N)，查找：O(M + N)

# 空间复杂度
# 存储：O(N)，查找：O(N)

class WordDistance:

    def __init__(self, words: List[str]):
        self.word_map = {}
        for i in range(len(words)):
            indexes = self.word_map.get(words[i], [])
            indexes.append(i)
            self.word_map[words[i]] = indexes
        

    def shortest(self, word1: str, word2: str) -> int:
        p1 = self.word_map[word1]
        p2 = self.word_map[word2]
        min_val = float('inf')
        i, j  = 0, 0
        while i < len(p1) and j < len(p2):
            wp1 = p1[i]
            wp2 = p2[j]
            if wp1 < wp2:
                min_val = min(min_val, wp2 - wp1)
                i += 1
            else:
                min_val = min(min_val, wp1 - wp2)
                j += 1
                
        return min_val
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)