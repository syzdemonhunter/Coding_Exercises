# https://leetcode.com/problems/rectangle-area/
# T: O(1)
# S: O(1)

class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        area_A = (C - A)*(D - B)
        area_B = (G - E)*(H - F)
        
        left = max(A, E)
        right = min(C, G)
        top = min(D, H)
        bottom = max(B, F)
        
        overlap = 0
        if right > left and top > bottom:
            overlap = (right - left)*(top - bottom)
        return area_A + area_B - overlap
        