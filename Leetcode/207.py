# https://leetcode.com/problems/course-schedule/
# T: O(V + E)
# S: O(n)
# BFS

import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        result = numCourses
        
        for pair in prerequisites:
            indegree[pair[0]] += 1
            
        q = collections.deque([])
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
                
        while q:
            pre = q.popleft()
            result -= 1
            for pair in prerequisites:
                if pair[1] == pre:
                    indegree[pair[0]] -= 1
                    if indegree[pair[0]] == 0:
                        q.append(pair[0])
                    
        return result == 0
                
                
            
        
        
        