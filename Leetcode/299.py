# https://leetcode.com/problems/bulls-and-cows/
# T: O(n)
# S: O(1)

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        dic = {}
        
        for idx, s in enumerate(secret):
            if guess[idx] == s:
                bulls += 1
            else:
                dic[s] = dic.get(s, 0) + 1
                
        for idx, s in enumerate(secret):
            if (guess[idx] != s) and (dic.get(guess[idx], 0) != 0):
                cows += 1
                dic[guess[idx]] -= 1
                
        return str(bulls) + 'A' + str(cows) + 'B'