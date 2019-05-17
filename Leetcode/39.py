# https://leetcode.com/problems/combination-sum/
# T: O(n^(target/min))
# S: O(target/min)

class Solution(object):
    def dfs(self, nums, start, elem, result, target):
        if target == 0:
            result.append(elem[:])
        if target < 0:
            return
        for i in range(start, len(nums)):
            if nums[i] > target:
                break
            elem.append(nums[i])
            self.dfs(nums, i, elem, result, target - nums[i])
            elem.pop()
            
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        result = []
        candidates.sort()
        self.dfs(candidates, 0, [], result, target)
        return result
        
        