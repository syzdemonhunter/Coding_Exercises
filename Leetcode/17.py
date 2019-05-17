# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# https://www.youtube.com/watch?v=KAJnbsikSC8&t=966s
# T: O(4^n * n)
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        
        digit_map = {
            0: '0',
            1: '1',
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz'
            
        }
        
        result = ['']
        for digit in digits:
            tmp_list = []
            for ch in digit_map[int(digit)]:
                for string in result:
                    tmp_list.append(string + ch)
                    
            result = tmp_list
            
        return result
        
        
        
        
        