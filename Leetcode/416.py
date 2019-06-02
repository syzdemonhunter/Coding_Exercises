# https://leetcode.com/problems/partition-equal-subset-sum/
# backtracking + memoization. 
# Time complexity: O(n*m), space complexity: O(n*m), where n = len(nums), m = sum(nums).

class Solution:
    def canPartition(self, nums: 'List[int]') -> 'bool':
        def backtrack(i, target):
            if target == 0:
                return True
            if i == len(nums) or target < 0:
                return False
            if (i, target) in dic:
                return dic[(i, target)]
            for j in range(i, len(nums)):
                if backtrack(j+1, target-nums[j]):
                    dic[(i, target)] = True
                    return True
            dic[(i, target)] = False
            return False
              
        summ = sum(nums)
        target = summ / 2
        if int(target) != target:
            return False
        dic = {}
        return backtrack(0, target)
        
        