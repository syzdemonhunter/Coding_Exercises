# https://leetcode.com/problems/sparse-matrix-multiplication/
# 一种时间复杂度为 O(m*n*l) 的办法
# 这种办法比较巧妙，通过初始化结果矩阵，然后把非零位逐个累乘累加的办法，而不是按照原来的矩阵乘法顺序在做。
# S: O(m*l) 
# A: m*n, B:n*l

class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        m, n = len(A), len(A[0])
        l = len(B[0])
        
        C = [[0]*l for i in range(m)]
        
        for i in range(m):
            for j in range(n):
                if A[i][j] != 0:
                    for t in range(l):
                        C[i][t] += A[i][j]*B[j][t]
                        
        return C
        