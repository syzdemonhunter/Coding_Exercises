# https://leetcode.com/problems/restore-ip-addresses/
# https://www.jiuzhang.com/solution/restore-ip-addresses/#tag-other-lang-python
# 典型的DFS，有个坑需要注意：
# 切出来的字符有可能是“007”， “00”之类的，需要跳过
# T: O(3^4)
# S: O(n)

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12:
            return []
        result = []
        self.dfs(s, [], result)
        return result
    
    def dfs(self, s, path, result):
        if len(s) > (4 - len(path))*3:
            return
        if not s and len(path) == 4:
            result.append('.'.join(path))
        for i in range(1, 4):
            if i <= len(s):
                number = int(s[:i]) # 切出来的字符有可能是“007”， “00”之类的，需要跳过
                if str(number) == s[:i] and number <= 255:
                    self.dfs(s[i:], path + [s[:i]], result)