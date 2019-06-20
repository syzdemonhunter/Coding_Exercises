# https://leetcode.com/problems/paint-house/
# T: O(n)
# S: O(1)

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs or len(costs) == 0:
            return 0
        
        for i in range(1, len(costs)):
            costs[i][0] += min(costs[i - 1][1], costs[i - 1][2])
            costs[i][1] += min(costs[i - 1][0], costs[i - 1][2])
            costs[i][2] += min(costs[i - 1][0], costs[i - 1][1])
            
        n = len(costs) - 1
        return min(min(costs[n][0], costs[n][1]), costs[n][2])
        