# https://leetcode.com/problems/encode-and-decode-tinyurl/
# https://www.youtube.com/watch?v=h60TlAmrpuM&t=1155s

import string, random, math

class Codec:
    def __init__(self):
        self.long_short = {}
        self.short_long = {}
        self.letters = string.ascii_letters + string.digits
        
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        def short_address():
            res = ''
            tmp = ''
            for _ in range(6):
                tmp = random.choice(list(self.letters))
                res += tmp
            return res
            
        if longUrl in self.long_short:
            return 'http://tinyurl.com/' + self.long_short[longUrl]
        else:
            suffix = short_address()
            self.long_short[longUrl] = suffix
            self.short_long[suffix] = longUrl
            return 'http://tinyurl.com/' + suffix
            
    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        shortUrl_suffix = shortUrl.split('/')[-1]
        if shortUrl_suffix in self.short_long:
            return self.short_long[shortUrl_suffix]
        
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

# 26 letters (upper lower) * 2 = 52, 0 ~ 9, 62
# short URL /
# # ? !
# A a