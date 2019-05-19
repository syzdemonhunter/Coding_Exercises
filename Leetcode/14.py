# https://leetcode.com/problems/longest-common-prefix/
# T: O(nk)
# S: O(k)

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        zip_strs = map(list, zip(*strs))
        result = ''
        
        for i in list(zip_strs):
            if [i[0]] * len(i) == i:
                result += i[0]
            else:
                break
                
        return result