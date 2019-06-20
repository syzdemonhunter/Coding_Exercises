# https://leetcode.com/problems/encode-and-decode-strings/
# T: O(n)
# S: O(n)

class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        sb = ''
        for st in strs:
            sb += str(len(st)) + '/' + st
        return sb
        
    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        result = []
        i = 0
        while i < len(s):
            slash = s[i:].index('/') + i
            size = int(s[i:slash])
            result.append(s[slash + 1: slash + size + 1])
            i = slash + size + 1
        return result

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))