# https://leetcode.com/problems/validate-ip-address/

class Solution(object):
    def validIPAddress(self, IP):
        hex_number = "1234567890abcdefABCDEF"
        
        if IP.count(".") == 3: 
            for s in IP.split("."):
                if not s.isdigit() or str(int(s)) != s or int(s) < 0 or int(s) > 255: 
                    return "Neither"
            return "IPv4"
        
        if IP.count(":") == 7:
            for s in IP.split(":"):
                if not s or not s.isalnum() or len(s) > 4 or any(char not in hex_number for char in s): 
                    return "Neither"
            return "IPv6"
        
        return "Neither"
        