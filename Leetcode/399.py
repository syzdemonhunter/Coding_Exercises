# https://leetcode.com/problems/evaluate-division/
# http://zxi.mytechroad.com/blog/graph/leetcode-399-evaluate-division/

# T: O(e + q): e: # of equations, q: # of queries
# S: O(e)

class Solution:
    def calcEquation(self, equations, values, queries):
        def find(x):
            if x != U[x][0]:
                px, pv = find(U[x][0])
                U[x] = (px, U[x][1] * pv)
            return U[x]
    
        def divide(x, y):
            px, vx = find(x) 
            py, vy = find(y)
            if px != py: return -1.0
            return vx / vy # vx: 
    
        U = {}
        for (x, y), v in zip(equations, values):      
            if x not in U and y not in U:
                U[x] = (y, v) 
                U[y] = (y, 1.0) 
            elif x not in U:
                U[x] = (y, v) 
            elif y not in U:
                U[y] = (x, 1.0 / v) 
            else:
                px, vx = find(x) 
                py, vy = find(y)
                U[px] = (py, v / vx * vy) 
    
        ans = [divide(x, y) if x in U and y in U else -1 for x, y in queries]
        return ans