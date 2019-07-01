# https://leetcode.com/problems/range-sum-query-immutable/submissions/

class NumArray:
    # T: O(n)
    def __init__(self, nums: List[int]):
        self.total = [0]*(len(nums) + 1)
        for i in range(len(nums)):
            self.total[i + 1] = self.total[i] + nums[i]
    # T: O(1)
    def sumRange(self, i: int, j: int) -> int:
        return self.total[j + 1] - self.total[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)