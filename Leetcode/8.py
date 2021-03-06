# https://leetcode.com/problems/string-to-integer-atoi/
# T: O(n)
# S: O(1)

class Solution:
    def myAtoi(self, str: str) -> int:
        str_list = list(str.strip())
        
        if len(str_list) == 0:
            return 0
        if str_list[0] == '-':
            sign = -1
        else:
            sign = 1
            
        if str_list[0] in ('-', '+'):
            del str_list[0]
            
        result, i = 0, 0
        while i < len(str_list) and str_list[i].isdigit():
            result = result*10 + ord(str_list[i]) - ord('0')
            i += 1
            
        return max(-2**31, min(sign*result, 2**31-1))
        