# https://leetcode.com/problems/valid-number/
# 你看哪家面经有再准备，没有的话就放弃吧。狂考corner case
# T: O(n)
# S: O(1)

class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        number_seen = False
        point_seen = False
        e_seen = False
        number_after_e = True
        
        for i in range(len(s)):
            if ord(s[i]) >= ord('0') and ord(s[i]) <= ord('9'):
                number_seen = True
                number_after_e = True
                
            elif s[i] == '.':
                if e_seen or point_seen:
                    return False
                point_seen = True
                
            elif s[i] == 'e':
                if e_seen or not number_seen:
                    return False
                e_seen = True
                number_after_e = False
                
            elif s[i] == '+' or s[i] == '-':
                if i != 0 and s[i - 1] != 'e':
                    return False
            else:
                return False
            
        return number_seen and number_after_e
            
            
            
        