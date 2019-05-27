# https://leetcode.com/problems/remove-comments/
# T: O(n)
# S: O(n)

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res, buffer, blk_cmt_open = [], '', False
        for line in source:
            i = 0
            while i < len(line):
                char = line[i]
                if char == '/' and i + 1 < len(line) and line[i + 1] == '/' and not blk_cmt_open:
                    i = len(line)
                elif char == '/' and i + 1 < len(line) and line[i + 1] == '*' and not blk_cmt_open:
                    blk_cmt_open = True
                    i += 1
                elif char == '*' and (i + 1) < len(line) and line[i + 1] == '/' and blk_cmt_open:
                    blk_cmt_open = False
                    i += 1
                elif not blk_cmt_open:
                    buffer += char
                i += 1
                
            if buffer and not blk_cmt_open:
                res.append(buffer)
                buffer = ''
                
        return res
        
        