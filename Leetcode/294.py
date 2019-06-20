# https://leetcode.com/problems/flip-game-ii/
# T: O(2^N) 不确定
# S: O(2^N)

class Solution:
    def canWin(self, s: str) -> bool:
        if not s or len(s) == 0:
            return False
        
        dic = {}
        return self.helper(s, dic)
    
    def helper(self, s, dic):
        if s in dic:
            return dic[s]
        for i in range(len(s) - 1):
            if s[i] == '+' and s[i + 1] == '+':
                opponent = s[:i] + '--' + s[i + 2:]
                if not self.helper(opponent, dic):
                    dic[s] = True
                    return True
        dic[s] = False
        return False
            
        