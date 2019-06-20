# https://leetcode.com/problems/palindrome-permutation-ii/
# T: ???
# S: O(n)

class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        odd = 0
        mid = ''
        path = []
        dic = {}
        
        for i in range(len(s)):
            c = s[i]
            dic[c] = dic.get(c, 0) + 1
            odd += 1 if dic[c] % 2 != 0 else -1
        
        if odd > 1:
            return []
        
        result = []
        for k, v in dic.items():
            if v % 2 != 0:
                mid += k
            for i in range(v//2):
                path.append(k)
        
        self.dfs(path, mid, [False]*len(path), '', result)
        return result
                
    def dfs(self, path, mid, used, sb, result):
        if len(sb) == len(path):
            result.append(sb + mid + sb[::-1])
            sb = sb[::-1]
            return
        
        for i in range(len(path)):
            if i > 0 and path[i] == path[i - 1] and not used[i - 1]:
                continue
            if not used[i]:
                used[i] = True
                self.dfs(path, mid, used, sb + str(path[i]), result)
                used[i] = False
                
        
        
        