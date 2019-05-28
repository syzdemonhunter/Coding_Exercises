# https://leetcode.com/problems/add-and-search-word-data-structure-design/
# 可以说, 这道题是 442. 实现 Trie (前缀树) 的升级版.
# 只需要在查询的时候将 '.' 处理为回溯即可, 即遇到 '.' 则需要访问每一个子节点判断是否有匹配.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if not word:
            return False
        return self.search_helper(self.root, word, 0)
    
    def search_helper(self, node, word, index):
        if not node:
            return False
        
        if index >= len(word):
            return node.is_word
        
        char = word[index]
        if char != '.':
            return self.search_helper(node.children.get(char), word, index + 1)
        
        for child in node.children:
            if self.search_helper(node.children[child], word, index + 1):
                return True
        return False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)