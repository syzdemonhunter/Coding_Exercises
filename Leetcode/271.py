# https://leetcode.com/problems/encode-and-decode-strings/
# T: O(nk)
# S: O(n)

class Codec:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    # " " -> ": " to separate different words
    # ":" -> "::" to identify ":"
    def encode(self, strs):
        # write your code here
        encoded = []
        for string in strs:
            for char in string:
                if char == ":":
                    encoded.append("::")
                else:
                    encoded.append(char)
            
            encoded.append(": ")
        
        # the res will always be ended with ": "
        # such as "lint: code: love: you: "
        return "".join(encoded)
                    

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, s):
        # write your code here
        res = []
        
        idx = 0
        length = len(s)
        tmp_str = []
        
        # length - 1 because it always ends with ": "
        while idx < length - 1:
            if s[idx] == ":":
                if s[idx + 1] == ":":
                    tmp_str.append(":")
                    idx += 2
                elif s[idx + 1] == " ":
                    res.append("".join(tmp_str))
                    tmp_str = []
                    idx += 2
            else:
                tmp_str.append(s[idx])
                idx += 1
        
        return res
                

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))