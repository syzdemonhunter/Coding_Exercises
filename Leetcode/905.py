# https://leetcode.com/problems/sort-array-by-parity/
# T: O(n)
# S: O(1)

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        if not A:
            return []
        
        if len(A) == 1:
            return A
        
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] % 2 != 0:
                A[i], A[j] = A[j], A[i]
                j -= 1
                
            else:
                i += 1
                
        return A
        