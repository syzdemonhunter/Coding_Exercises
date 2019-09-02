# https://leetcode.com/problems/unique-word-abbreviation/
# T: O(n)
# S: O(n)

class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.dic = {}
        for word in dictionary:
            key = self.get_key(word)
            if key in self.dic:
                if self.dic[key] != word:
                    self.dic[key] = ''
            else:
                self.dic[key] = word
        

    def isUnique(self, word: str) -> bool:
        return self.get_key(word) not in self.dic or\
               self.dic[self.get_key(word)] == word
        

    def get_key(self, s):
        if len(s) <= 2:
            return s
        return s[0] + str(len(s) - 2) + s[len(s) - 1]

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)