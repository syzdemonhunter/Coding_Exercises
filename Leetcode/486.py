# https://leetcode.com/problems/predict-the-winner/
# T: O(n^2)
# S: O(n)

"""
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 0:
            return False
        
        n = len(nums)
        dp = [[0]*n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][i]= nums[i]
                else:
                    dp[i][j] = max(nums[i] - dp[i + 1][j],
                                nums[j] - dp[i][j - 1])
        return dp[0][n - 1] >= 0   
"""    
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 0:
            return False
        
        n = len(nums)
        dp = [0]*n
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i]= nums[i]
                else:
                    dp[j] = max(nums[i] - dp[j],
                                nums[j] - dp[j - 1])
        return dp[n - 1] >= 0 

