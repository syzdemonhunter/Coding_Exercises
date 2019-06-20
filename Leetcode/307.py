# https://leetcode.com/problems/range-sum-query-mutable/
# https://leetcode.com/problems/range-sum-query-mutable/discuss/75730/148ms-Python-solution-Binary-Indexed-Tree
# Binary Index Tree：解决问题：前n项和
# 我觉得不太可能考

# Use self.c to represent Binary Indexed Tree. Section sums are stored in self.c[1..len(nums)]. x & -x is lowbit function, which will return x's rightmost bit 1, e.g. lowbit(7) = 1, lowbit(20) = 4.

# self.c[1] = nums[0]

# self.c[2] = nums[0] + nums[1]

# self.c[3] = nums[2]

# self.c[4] = nums[0] + nums[1] + nums[2] + nums[3]

# self.c[5] = nums[4]

# self.c[6] = nums[4] + nums[5]

# self.c[7] = nums[6]

# self.c[8] = nums[0] + nums[1] + nums[2] + nums[3] + nums[4] + nums[5] + nums[6] + nums[7]



class NumArray:
    # T: O(nlogn)
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums
        self.tree = [0]*(self.n + 1)
        for i in range(self.n):
            k = i + 1
            while k <= self.n:
                self.tree[k] += nums[i]
                k += (k & -k)
                
    # O(logn)
    def update(self, i: int, val: int) -> None:
        diff = val - self.nums[i]
        self.nums[i] = val
        i += 1
        while i <= self.n:
            self.tree[i] += diff
            i += (i & -i)
            
    # O(logn)
    def sumRange(self, i: int, j: int) -> int:
        result = 0
        j += 1
        while j:
            result += self.tree[j]
            j -= (j & -j)
        while i:
            result -= self.tree[i]
            i -= (i & -i)
        return result
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)