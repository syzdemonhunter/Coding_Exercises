# https://leetcode.com/problems/roman-to-integer/
# T: O(n)
# S: O(1)

class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        number_dict = {'I':1, 'V':5, 'X':10, 'L':50,
                       'C':100, 'D':500, 'M':1000}
        
        for i in range(len(s)):
            if i > 0 and number_dict[s[i]] > number_dict[s[i - 1]]:
                result += number_dict[s[i]] - 2*number_dict[s[i - 1]]
                
            else:
                result += number_dict[s[i]]
                
        return result
        