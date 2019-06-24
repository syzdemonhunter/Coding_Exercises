# https://leetcode.com/problems/palindrome-partitioning-ii/
# T: O(n^2)
# S: O(n^2)

class Solution:
    def minCut(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0
        
        s_len = len(s)
        cuts = [0]*s_len
        is_pa = [[False]*s_len for _ in range(s_len)]
        
        for i in range(s_len):
            min_val = i
            for j in range(i + 1):
                if s[i] == s[j] and (i - j < 2 or is_pa[j + 1][i - 1]):
                    is_pa[j][i] = True
                    min_val = 0 if j == 0 else min(min_val, cuts[j - 1] + 1)
            cuts[i] = min_val
            
        return cuts[s_len - 1]
                    