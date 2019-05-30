# https://leetcode.com/problems/fraction-to-recurring-decimal/
# # https://www.youtube.com/watch?v=zy8sJ_Wx7y8

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        neg_flag = numerator*denominator < 0
        num = abs(numerator)
        den = abs(denominator)
        num_list = []
        cnt = 0
        loop_dict = {}
        loop_str = None
        
        while True:
            num_list.append(str(num//den))
            cnt += 1
            num = 10*(num % den) # 20/3
            if num == 0: #整除
                break
            loc = loop_dict.get(num) # 1/3 -> 10/3 -> 1/3
            if loc:
                loop_str = ''.join(num_list[loc:cnt])
                break
            loop_dict[num] = cnt 
        ans = num_list[0]
        
        if len(num_list) > 1: # 是否有小数
            ans += '.'
            
        if loop_str:
            ans += ''.join(num_list[1:len(num_list) - len(loop_str)]) \
                           + '(' + loop_str + ')'
        else:
            ans += ''.join(num_list[1:])
            
        if neg_flag:
            ans = '-' + ans
            
        return ans

            