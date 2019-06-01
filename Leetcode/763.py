# https://leetcode.com/problems/partition-labels/
# https://www.youtube.com/watch?v=s-1W5FDJ0lw
# T: O(n)
# S: O(26/128)

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last_idx = {}
        for i, ch in enumerate(S):
            last_idx[ch] = i
        start = end = 0
        result = []
        
        for i, ch in enumerate(S):
            end = max(end, last_idx[ch])
            if i == end:
                result.append(end - start + 1)
                start = end + 1
        return result