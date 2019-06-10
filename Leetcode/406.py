# https://leetcode.com/problems/queue-reconstruction-by-height/
# https://leetcode.com/problems/queue-reconstruction-by-height/discuss/167308/Python-solution
# T: O(n^2)
# S: O(n)

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key = lambda x: (-x[0], x[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
        return res
        