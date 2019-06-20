# https://leetcode.com/problems/h-index/
'''
# T: O(nlogn)
# S: O(1)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        result = 0
        while result < len(citations) and citations[len(citations) - 1 - result] > result:
            result += 1
            
        return result
'''
# T: O(n)
# S: O(n)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        papers = [0]*(n + 1)  # papers[i] is the number of papers with i citations.
        for c in citations:
            papers[min(n, c)] += 1  # All papers with citations larger than n is count as n.
        i = n
        s = papers[n]  # sum of papers with citations >= i
        while i > s:
            i -= 1
            s += papers[i]
        return i

                