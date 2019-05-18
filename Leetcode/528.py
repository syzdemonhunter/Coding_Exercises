# https://www.youtube.com/watch?v=ORP4cxNuMSs
# T: O(n)
# S: O(n)

# use w_run to get weight assigned to each index
# use binary search to find the first integer that is greater or equal to the target(random) number

import itertools
class Solution(object):
    import itertools
    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.w_run = [0]*len(w)
        self.w_run[0] = w[0]
        for i in range(1, len(w)):
            self.w_run[i] = self.w_run[i - 1] + w[i]
        
    def pickIndex(self):
        """
        :rtype: int
        """
        target = random.randint(1, self.w_run[-1])
        start, end = 0, len(self.w_run) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if self.w_run[mid] == target:
                return mid
            elif self.w_run[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
                
        return start
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()