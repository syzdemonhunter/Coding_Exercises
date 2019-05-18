# https://leetcode.com/problems/backspace-string-compare/
# T: O(n)
# S: O(n)

class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def helper(word):
            word_stack = []
            
            for w in word:
                if w != '#':
                    word_stack.append(w)
                else:
                    if not word_stack:
                        pass
                    else:
                        word_stack.pop()
                        
            return ''.join(word_stack)
        
        return helper(S) == helper(T)