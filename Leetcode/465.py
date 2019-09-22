# https://leetcode.com/problems/optimal-account-balancing/
# T: O(n!) 不确定
# S: O(n)

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        self.result = sys.maxsize
        dic = {}
        for transaction in transactions:
            dic[transaction[0]] = dic.get(transaction[0], 0) - transaction[2]
            dic[transaction[1]] = dic.get(transaction[1], 0) + transaction[2]
            
        debt = []
        for value in dic.values():
            if value != 0:
                debt.append(value)
                
        self.helper(debt, 0, 0)
        return self.result
    
    def helper(self, debt, start, count):
        while start < len(debt) and debt[start] == 0:
            start += 1
            
        if start == len(debt):
            self.result = min(self.result, count)
            return
        
        for i in range(start + 1, len(debt)):
            if (debt[start] < 0 and debt[i] > 0) or (debt[start] > 0 and debt[i] < 0):
                debt[i] += debt[start]
                self.helper(debt, start + 1, count + 1)
                debt[i] -= debt[start]
                
        