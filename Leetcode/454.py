# https://leetcode.com/problems/4sum-ii/
# T: O(n^2)
# S: O(n)

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        result = 0
        dic = {}
        for a in A:
            for b in B:
                total = a + b
                dic[total] = dic.get(total, 0) + 1
                
        for c in C:
            for d in D:
                total = -c - d
                result += dic.get(total, 0)
                
        return result
        
    
        