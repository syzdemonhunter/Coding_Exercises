# https://leetcode.com/problems/word-pattern/
# 这道题肯定会考到
# T: O(n^2)
# S: O(1)

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        arr = str.split(' ')
        if len(arr) != len(pattern):
            return False
        
        dic = {}
        for i in range(len(arr)):
            c = pattern[i]
            if c in dic:
                if dic[c] == arr[i]:
                    continue
                else:
                    return False
                
            else:
                if arr[i] not in dic.values():
                    dic[c] = arr[i]
                else:
                    return False
                
        return True
                
                