# https://algocasts.io/episodes/17WMX8pj
# T: O(n)
# S: O(1)


class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N in (0, 1):
            return N
        
        pre_pre = 0
        pre = 1
        
        for i  in range(2, N+1):
            current = pre_pre + pre
            pre_pre = pre
            pre = current
            
        return pre
        