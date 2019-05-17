# https://leetcode.com/problems/jewels-and-stones/
# T: O(m + n)
# S: O(k): k = size of S


class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        if not J or not S:
            return 0
        jew_dict = {}
        for j in J:
            if j not in jew_dict:
                jew_dict[j] = 0
                
        for s in S:
            if s in jew_dict:
                jew_dict[s] += 1
                
        result = 0
        for v in jew_dict.values():
            result += v
            
        return result