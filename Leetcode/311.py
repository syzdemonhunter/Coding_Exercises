# https://leetcode.com/problems/sparse-matrix-multiplication/
# T: O(m*n*l)
# S: O(m*l)

class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        m, n = len(A), len(A[0])
        l = len(B[0])
        result = [[0]*l for i in range(m)]
        
        for i in range(m):
            for j in range(n):
                if A[i][j] != 0:
                    for k in range(l):
                        if B[j][k] != 0:
                            result[i][k] += A[i][j]*B[j][k]
                            
        return result
        