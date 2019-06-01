# https://leetcode.com/problems/to-lower-case/
# T: O(n)
# S: O(n)

class Solution:
    def toLowerCase(self, str: str) -> str:
        result = ''
        for letter in str:
            if (ord(letter) > ord('Z')) or (ord(letter) < ord('A')):
                result += letter
                
            else:
                tmp = ord(letter) + (ord('a') - ord('A'))
                result += chr(tmp)
                
        return result