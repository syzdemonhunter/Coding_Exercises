# https://leetcode.com/problems/minimum-window-substring/
# 非常重要！不熟多做几遍，背也要背下来！！
# T: O(n)
# S: O(1)

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''
        
        cnt = collections.Counter(t)            #hash table to store char frequency
        total = len(t)                         #total number of chars we care
        start, end = 0, 0
        i = 0
        
        for j, char in enumerate(s, 1):          #index j from 1
            if cnt[char] > 0:
                total -= 1
            cnt[char] -= 1
            if total == 0:                     #match all chars
                while i < j and cnt[s[i]] < 0:  #remove chars to find the real start
                    cnt[s[i]] += 1
                    i += 1
                cnt[s[i]] += 1                  #make sure the first appearing char satisfies cnt[char]>0
                total += 1                     #we missed this first char, so add total by 1
                if end == 0 or j - i < end - start:  #update window
                    start, end = i, j
                i += 1                           #update i to start+1 for next window
                
        return s[start:end]