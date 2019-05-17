# https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode(object):
    def __init__(self, end=False):
        self.children = []
        for i in range(26):
            self.children.append(None)
        self.end = end
        
    def set_end(self):
        self.end = True
        
    @property    
    def is_end(self):
        return self.end

    
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        cur = self.root
        for letter in word:
            idx = ord(letter) - ord('a')
            if not cur.children[idx]:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]
        cur.set_end()
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for letter in word:
            idx = ord(letter) - ord('a')
            if not cur.children[idx]:
                return False
            else:
                cur = cur.children[idx]
        return cur.is_end
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for letter in prefix:
            idx = ord(letter) - ord('a')
            if not cur.children[idx]:
                return False
            else:
                cur = cur.children[idx]
        return True
            


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)