# https://leetcode.com/problems/task-scheduler/
# https://www.jiuzhang.com/solution/task-scheduler/#tag-highlight-lang-python
#仔细分析题意可知，最后所消耗的时间主要受制于出现次数最多的那个字母，所以我们可以推导出，所消耗的时间为 count(字母最多出现次数) * k - (其他字母贡献)

#There are two cases: 
# (1) We don't need idle and CPU will keep working. In this case, we need the same number of intervals to tasks. 
# (2) There should be idle and we find the most frequent tasks and use the equation "(k-1) * (n+1) + p" for calculation, where k is the frequency and p is the number of tasks appearing k times in input array. 

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        task_to_times = {}
        for task in tasks:
            if task not in task_to_times:
                task_to_times[task] = 0
            task_to_times[task] += 1
            
        longest = max(task_to_times.values())
        
        ans = (longest - 1)*(n + 1)
        for times in task_to_times.values():
            if times == longest:
                ans += 1
                
        return max(len(tasks), ans)
        