# https://leetcode.com/problems/combination-sum-ii/
# T: O(2^n)
# S: O(n)

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates or len(candidates) == 0:
            return []
        
        candidates.sort()
        result = []
        self.helper(result, [], candidates, target)
        return result
        
    def helper(self, result, path, candidates, target):
        if target < 0:
            return

        if target == 0:
            result.append(path)
            return

        for i in range(len(candidates)):
            if candidates[i] > target:
                continue
                
            if i > 0 and candidates[i] == candidates[i - 1]:
                continue
    
            self.helper(result, path + [candidates[i]], candidates[i + 1:], target - candidates[i])
        
        