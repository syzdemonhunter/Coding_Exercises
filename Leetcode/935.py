# https://leetcode.com/problems/knight-dialer/
# https://www.youtube.com/watch?v=vjRcT-7b0yA&feature=youtu.be&t=247
# T: O(n)
# S: O(1)

class Solution(object):
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        neighbors = {
        0:(4,6),
        1:(6,8),
        2:(7,9),
        3:(4,8),
        4:(0,3,9),
        5:(), # 5 has no neighbors
        6:(0,1,7),
        7:(2,6),
        8:(1,3),
        9:(2,4)
        }
        mod = 10**9 + 7
        
        current_counts = [1]*10
        for _ in range(N-1):
            next_counts = [0]*10
            for key in range(10):
                for dist_key in neighbors[key]:
                    next_counts[dist_key] = \
                    (next_counts[dist_key] + current_counts[key]) % mod
            current_counts = next_counts
        return sum(current_counts) % mod