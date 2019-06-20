# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# T: O(4^n)
# S: O(n)

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:        
        if not digits or len(digits) == 0:
            return []
        
        dic = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = []
        self.dfs(digits, dic, 0, "", res)
        return res
    
    def dfs(self, digits, dic, index, path, res):
        if len(path) == len(digits):
            res.append(path)
            return
        
        for j in dic[digits[index]]:
            self.dfs(digits, dic, index + 1, path + j, res)
    
    