# https://leetcode.com/problems/valid-square/
# T: O(1)
# S: O(1)

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        my_set = set([self.dist(p1, p2), 
                     self.dist(p1, p3),
                     self.dist(p1, p4),
                     self.dist(p2, p3),
                     self.dist(p2, p4),
                     self.dist(p3, p4)])
        
        return 0 not in my_set and len(my_set) == 2
    
    def dist(self, a, b):
        return (a[0] - b[0])**2 + (a[1] - b[1])**2
        
        
        