# https://leetcode.com/problems/integer-to-english-words/
# T: O(n)
# S: O(1)

class Solution:
    def __init__(self):
        self.lessThan20 = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten",\
                           "Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        self.tens = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        self.thousands = ["","Thousand","Million","Billion"]

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        result = ""
        i = 0
        while num > 0:
            if num % 1000 != 0:
                result = self.helper(num % 1000) + self.thousands[i] + " " + result
            num //= 1000
            i += 1
            
        return result.strip()
    
    def helper(self, num):
        if num == 0:
            return ""
        elif num < 20:
            return self.lessThan20[num] + " "
        elif num < 100:
            return self.tens[num//10] + " " + self.helper(num % 10)
        else:
            return self.lessThan20[num//100] + " Hundred " + self.helper(num % 100)            