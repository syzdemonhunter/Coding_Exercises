# https://leetcode.com/problems/min-cost-climbing-stairs/
# T: O(n)
# S: O(1)


class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if not cost:
            return 0
        
        cost_len = len(cost)
        if cost_len < 2:
            return cost[0]
        elif cost_len == 2:
            return min(cost[0], cost[1])
        first, second = cost[0], cost[1]
        
        for i in range(2, cost_len):
            cur = min(first, second) + cost[i]
            first = second
            second = cur
            
        return min(first, second)
        