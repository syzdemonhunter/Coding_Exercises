# https://leetcode.com/problems/course-schedule/
# T: O(|V|+|E|)
# S: O(|V|+|E|)

class Solution(object):
    def has_cycle(self, graph, visited, checked, v):
        if visited[v]:
            return True
        visited[v] = True
        for i in graph[v]:
            if not checked[i] and self.has_cycle(graph, visited, checked, i):
                return True
        checked[v] = True
        visited[v] = False
        return False

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not prerequisites or len(prerequisites) == 0 or numCourses <= 1:
            return True
        
        graph = []
        visited = []
        checked = []
        for i in range(numCourses):
            graph.append([])
            checked.append(False)
            visited.append(False)
        
        for item in prerequisites:
            graph[item[1]].append(item[0])
        for i in range(numCourses):
            if not checked[i] and self.has_cycle(graph, visited, checked, i):
                return False
        return True
        