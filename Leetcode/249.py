# https://leetcode.com/problems/group-shifted-strings/
# T: O(n*m)
# S: O(n)

import collections
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        result = []
        my_map = collections.defaultdict(list)
        for string in strings:
            offset = ord(string[0]) - ord('a')
            key = ''
            for i in range(len(string)):
                c = ord(string[i]) - offset
                if c < ord('a'):
                    c += 26
                key += chr(c)
                
            my_map[key].append(string)
            
        for key in my_map.keys():
            path = my_map[key]
            result.append(path)
            
        return result
            
        