# https://leetcode.com/problems/repeated-dna-sequences/submissions/
# T: O(n)
# S: O(n)

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen, repeated = set(), set()
        for i in range(len(s) - 9):
            tmp = s[i:i+10]
            if tmp in seen:
                repeated.add(tmp)
            else:
                seen.add(tmp)
        return list(repeated)
        