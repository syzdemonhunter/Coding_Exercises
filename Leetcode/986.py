# https://leetcode.com/problems/interval-list-intersections/
# Time complexity: O(m + n)
# Space complexity: O(1)

# s = max(a.start, b.start)
# e = min(a.end, b.end)
# if s <= e, there is an intersection

class Solution:
    def intervalIntersection(self, A: 'List[Interval]', B: 'List[Interval]') -> 'List[Interval]':
        if not A or not B:
            return []
        
        i, j, result = 0, 0, []
        while i < len(A) and j < len(B):
            s = max(A[i][0], B[j][0])
            e = min(A[i][1], B[j][1])
            if s <= e:
                result.append([s, e])
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        return result