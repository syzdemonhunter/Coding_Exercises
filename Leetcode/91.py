# https://leetcode.com/problems/decode-ways/
# T: O(n)
# S: O(1)


class Solution(object):
    def helper(self, a, b):
        return (a == "1" and b <= "9") or (a == "2" and b <= "6")
    
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        first = 1
        second = 1 if s[0] != '0' else 0
        for i in range(2, len(s) + 1):
            third = 0
            if s[i - 1] != '0':
                third += second
            if self.helper(s[i-2], s[i-1]):
                third += first
                
            first = second
            second = third
            
        return second
        