# https://leetcode.com/problems/repeated-dna-sequences/
# T: O(n)
# S: O(n)

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dic, s_tmp = {}, 'x' + s[:9]
        for i in range(9, len(s)):
            s_tmp = s_tmp[1:] + s[i]
            dic[s_tmp] = dic.get(s_tmp, 0) + 1
            
        return [k for k, v in dic.items() if v > 1]
        