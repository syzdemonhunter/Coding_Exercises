# https://leetcode.com/problems/reorder-log-files/
# T: O(nlogn)
# S: O(n)

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs, num_logs = {}, []
        for log in logs:
            i = log.index(" ")
            val = log[i+1:]
            if val[0].isdigit():
                num_logs.append(log)
            else:
                letter_logs[log] = val
                
        sorted_letter_logs = sorted(letter_logs, key = lambda x: (letter_logs[x], x))
        return sorted_letter_logs + num_logs
                
                
