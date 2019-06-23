# https://leetcode.com/problems/reverse-vowels-of-a-string/
# T: O(n)
# S: O(n)

class Solution:
    def reverseVowels(self, s: str) -> str:
        if not s or len(s) == 0:
            return s
        
        vowels = 'aeiouAEIOU'
        s_list = list(s)
        start, end = 0, len(s) - 1
        
        while start < end:
            while start < end and s_list[start] not in vowels:
                start += 1
            while start < end and s_list[end] not in vowels:
                end -= 1
                
            s_list[start], s_list[end] = s_list[end], s_list[start]
            start += 1
            end -= 1
            
        return ''.join(s_list)
                