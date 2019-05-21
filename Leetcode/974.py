# https://leetcode.com/problems/subarray-sums-divisible-by-k/
# Time Complexity: O(N)
# Space Complexity: O(K)

# About the problems - sum of contiguous subarray , prefix sum is a common technique.
# Another thing is if sum[0, i] % K == sum[0, j] % K, sum[i + 1, j] is divisible by by K.
# So for current index j, we need to find out how many index i (i < j) exit that has the same mod of K.
# Now it easy to come up with HashMap <mod, frequency>

class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        my_map = {}
        my_map[0] = 1
        count, total = 0, 0
        for a in A:
            total = (total + a) % K
            if total < 0:
                total += K # / Because -1 % 5 = -1, but we need the positive mod 4
            count += my_map.get(total, 0) 
            my_map[total] = my_map.get(total, 0) + 1
            
        return count
        
        
        