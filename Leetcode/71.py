# https://leetcode.com/problems/simplify-path/
# T: O(n)
# S: O(n)

class Solution:
    def simplifyPath(self, path: str) -> str:
        # 1. Simplify
        while "//" in path:
            path = path.replace("//", "/")
            
        #Edge cases
        if path == "/": 
            return path

        #Prepare for stack
        if path[0] == "/": 
            path = path[1:]
        if path[len(path)-1] == "/": 
            path = path[:len(path)-1]

        # 2. Stack
        path_stack = []
        path = path.split("/")
        for p in path:
            if p == "..":
                if len(path_stack) > 0: 
                    path_stack.pop()
            elif p == ".":
                pass
            else:
                path_stack.append(p)

        # 3. Parse -> Return
        path = "/".join(path_stack)
        return "/" + path
        