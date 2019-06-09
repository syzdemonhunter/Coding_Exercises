# https://leetcode.com/problems/bulls-and-cows/
# T: O(n)
# S: O(1)

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull, cow = 0, 0
        cache = {}
        for i, v in enumerate(secret):
            if v == guess[i]:
                bull += 1
            else:
                cache[v] = cache[v] + 1 if v in cache else 1
                
        for i, v in enumerate(guess):
            if v != secret[i] and v in cache and cache[v] > 0:
                cow += 1
                cache[v] -= 1
                
        return '{}A{}B'.format(bull, cow)
        