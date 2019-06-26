# https://leetcode.com/problems/paint-house-ii/
# T: O(n*k)
# S: O(1)

class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs or len(costs) == 0:
            return 0
        
        n, k = len(costs), len(costs[0])
        min1, min2 = -1, -1
        for i in range(n):
            last1 = min1
            last2 = min2
            min1, min2 = -1, -1
            
            for j in range(k):
                if j != last1:
                    costs[i][j] += 0 if last1 < 0 else costs[i - 1][last1]
                else:
                    costs[i][j] += 0 if last2 < 0 else costs[i - 1][last2]
                    
                if min1 < 0 or costs[i][j] < costs[i][min1]:
                    min2 = min1
                    min1 = j
                
                elif min2 < 0 or costs[i][j] < costs[i][min2]:
                    min2 = j
                    
        return costs[n - 1][min1]