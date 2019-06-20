# https://leetcode.com/problems/permutation-sequence/
# T: O(n)
# S: O(n)

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        result_tmp = [i for i in range(1, n + 1)]
        
        fact = [0]*n # fact： n的全排列个数
        fact[0] = 1
        for i in range(1, n):
            fact[i] = i*fact[i - 1]
            
        k = k - 1
        result = ''
        for i in range(n, 0, -1):
            index = k // fact[i - 1]
            k = k % fact[i - 1]
            result += str(result_tmp[index])
            result_tmp.remove(result_tmp[index])
            
        return result
        