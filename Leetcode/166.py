# https://leetcode.com/problems/fraction-to-recurring-decimal/
# T: O(n)
# S: O(n)

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'

        result = ''
        result += '-' if (numerator > 0)^(denominator > 0) else ''
        num_abs = abs(numerator)
        den_abs = abs(denominator)

        result += str(num_abs//den_abs)
        num_abs %= den_abs

        if num_abs == 0:
        	return result

        result += '.'
        my_map = {}
        my_map[num_abs] = len(result)

        while num_abs != 0:
        	num_abs *= 10
        	result += str(num_abs//den_abs)
        	num_abs %= den_abs
        	if num_abs in my_map:
        		index = my_map[num_abs]
        		result_list = list(result)
        		result_list.insert(index, '(')
        		result_list.append(')')
        		result = ''.join(result_list) 
        		break

        	else:
        		my_map[num_abs] = len(result)

        return result
            
        