# https://leetcode.com/problems/exclusive-time-of-functions/
# 中间含有递归调用，即后进先出。栈的思想
# T: O(n)
# S: O(n)

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        result = [0]*n
        ts_last = 0
        for log in logs:
            log = log.split(':')
            id, status, ts = int(log[0]), log[1], int(log[2])
            if status == 'start':
                if stack:
                    result[stack[-1]] += ts - ts_last
                stack.append(id)
            else:
                ts += 1
                result[stack.pop()] += ts - ts_last
            ts_last = ts
            
        return result
        