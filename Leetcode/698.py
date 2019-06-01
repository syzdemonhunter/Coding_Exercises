# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
# https://www.youtube.com/watch?v=r6I-ikllNDM
# T:O(n*sum)
# S: O(n*sum)

# k is group waiting to form(make up)
# fromindex is where we start to find the next number
# cursum is current sum which we making up to target now

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        visit = [0 for i in range(len(nums))]
        target = sum(nums) // k
        
        def dfs(k, from_idx, cur_sum):
            if k == 1 and cur_sum == target:
                return True
            if cur_sum == target:
                return dfs(k - 1, 0, 0)
            else:
                for i in range(from_idx, len(nums)):
                    if nums[i] + cur_sum <= target and not visit[i]:
                        visit[i] = 1
                        if dfs(k, i + 1, cur_sum + nums[i]):
                            return True
                        visit[i] = 0
                        
                return False
            
        if sum(nums) % k != 0 or k > sum(nums):
            return False
        return dfs(k, 0, 0)
        
        
        