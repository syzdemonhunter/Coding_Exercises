# https://leetcode.com/problems/water-and-jug-problem/
# T: < O(n)
# S: O(n)    

class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x + y < z:
            return False
        if x == z or y == z or x + y == z:
            return True
        return z % self.gcd(x, y) == 0
    
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)