# https://leetcode.com/problems/gas-station/
# https://www.cnblogs.com/boring09/p/4248482.html
# T: O(n)
# S: O(1)

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if len(gas) == 0 or len(cost) == 0 or len(gas) != len(cost):
            return -1
        start = 0
        remain = 0
        debt = 0
        
        for i in range(len(gas)):
            remain += gas[i] - cost[i]
            if remain < 0:
                debt += remain
                start = i + 1
                remain = 0
                
        return start if remain + debt >= 0 else -1
        