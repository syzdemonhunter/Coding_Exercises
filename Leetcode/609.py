# https://leetcode.com/problems/find-duplicate-file-in-system/
# T: O(n)
# S: O(n)

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)
        for path in paths:
            directory, *files = path.split(' ')
            for f in files:
                name, contect = f.split('(')
                dic[contect].append(directory + '/' + name)
        return [v for v in dic.values() if len(v) > 1]