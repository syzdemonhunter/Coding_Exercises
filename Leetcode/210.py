# https://leetcode.com/problems/course-schedule-ii/
# T: O(V + E)
# S: O(n)

import collections
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0]*numCourses
        result = [0]*numCourses
        k = 0
        for pair in prerequisites:
            indegree[pair[0]] += 1
            
        q = collections.deque([])
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
                result[k] = i
                k += 1
        while q:
            pre = q.popleft()
            for pair in prerequisites:
                if pair[1] == pre:
                    indegree[pair[0]] -= 1
                    if indegree[pair[0]] == 0:
                        q.append(pair[0])
                        result[k] = pair[0]
                        k += 1
                        
        return result if k == numCourses else []
                        
            
        