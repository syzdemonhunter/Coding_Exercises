# https://leetcode.com/problems/pancake-sorting/
# 找到最大的数字，假设它的下标是i
# 反转0到i之间的数字，使得A[i]变成第一个数
# 反转整个数组，让最大的数到末尾

# T: O(N^2)
# S: O(N)

class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        n = len(A)
        res = []
        for i in range(n):
            cur_max = max(A[0:n - i])
            j = 0
            while A[j] != cur_max:
                j += 1
            # should reverse j+1 elements
            A[:j + 1] = reversed(A[:j + 1])
            res.append(j + 1)
            # reverse all
            A[:n - i] = reversed(A[:n - i])
            res.append(n - i)
        return res