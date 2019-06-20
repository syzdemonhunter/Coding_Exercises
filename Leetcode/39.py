# https://leetcode.com/problems/combination-sum/
# T: O(2^n)
# S: O(n)

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates or len(candidates) == 0:
            return []
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
            self.helper(result, path + [candidates[i]], candidates[i:], target - candidates[i])
            