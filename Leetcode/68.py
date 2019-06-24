# https://leetcode.com/problems/text-justification/
# 这道题还是会考的。
# T: O(n)
# S: O(n)

class Solution:
    
    def _format(self, line, maxWidth):
        if len(line) == 1:
            return line[0] + " "*(maxWidth - len(line[0]))
        length = sum([len(w) for w in line])
        s, gaps = line[0], len(line) - 1
        
        for index, w in enumerate(line[1:]):
            if index < (maxWidth - length) % gaps:
                s = s + " " + " "*((maxWidth - length)//gaps) + w
            else:
                s = s + " "*((maxWidth - length)//gaps) + w
                
        return s
        
    def _formatLast(self, line, maxWidth):
        s = ' '.join(line)
        return s + " "*(maxWidth - len(s))
    
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        line, length = [], 0
        results = []
        for w in words:
            if length + len(w) + len(line) <= maxWidth:
                length += len(w)
                line.append(w)
            else:
                results.append(self._format(line, maxWidth))
                length = len(w)
                line = [w]
        if len(line):
            results.append(self._formatLast(line, maxWidth))
        return results