# https://leetcode.com/problems/minimum-time-difference/
# T: O(24*60)
# S: O(24*60)

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        mark = [False]*(24*60)
        
        for time in timePoints:
            t = time.split(':')
            hour = int(t[0])
            minute = int(t[1])
            
            if mark[hour*60 + minute]:
                return 0
            
            mark[hour*60 + minute] = True
            
        result = sys.maxsize
        pre, first = -1, -1

        for i in range(len(mark)):
            if mark[i]:
                if first == -1:
                    first = i
                else:
                    result = min(result, i - pre)
                pre = i

        result = min(result, (first + 24*60 - pre))
        return result
                    
            
            