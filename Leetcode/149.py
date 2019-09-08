# https://leetcode.com/problems/max-points-on-a-line/
# T: O(n^2)
# S: O(n)

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if not points or len(points) == 0:
            return 0
        if len(points) < 2:
            return len(points)
        
        d = collections.defaultdict(int) 
        result = 0
        for i in range(len(points)):
            d.clear()
            overlap = 0
            curmax = 0
            for j in range(i + 1, len(points)):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                
                if dx == 0 and dy == 0:
                    overlap += 1
                    continue
                    
                gcd = self.getGcd(dx, dy)
                dx //= gcd
                dy //= gcd
                d[(dx,dy)] += 1
                curmax = max(curmax, d[(dx,dy)])
                
            result = max(result, curmax + overlap + 1)
        return result

    def getGcd(self, a, b):
        if b == 0: 
            return a
        return self.getGcd(b, a % b)