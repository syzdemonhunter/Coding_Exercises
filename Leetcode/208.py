# https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    # Time O(n): n: word.length()
    # O(num of TrieNode*26) = O(num of Words * len(word) * 26)
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for w in word:
            node = node.children[w]
        node.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.is_word
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for i in prefix:
            if i not in node.children:
                return False
            node = node.children[i]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)