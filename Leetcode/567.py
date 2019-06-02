# https://leetcode.com/problems/permutation-in-string/
# 先扫一遍字符串s1，统计各个字母的个数，取s2前s1长度个字符，匹配个数是否相符，若不相符，去除最前面的字符，加入后一个字符，重新比对，直至个数匹配，或扫描完s2。

import collections

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        need = collections.Counter(s1)
        missing = l1
        for i, c in enumerate(s2):
            if c in need:
                if need[c] > 0:
                    missing -= 1
                need[c] -= 1
    
            if i >= l1 and s2[i - l1] in need:
                need[s2[i - l1]] += 1
                if need[s2[i - l1]] > 0:
                    missing  += 1

            if missing == 0:
                return True
                
        return False
        
        