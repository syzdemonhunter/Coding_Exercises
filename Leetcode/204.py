# https://leetcode.com/problems/count-primes/
# T: O(n log log n)
# S: O(n)

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        
        is_prime = [True] * n
        is_prime[0], is_prime[1] = False, False
        
        for i in range(2, int((n-1)**0.5) + 1):
            if is_prime[i]:
                for j in range(i**2, n, i):
                    is_prime[j] = False
                    
        return len([x for x in range(2, n) if is_prime[x]])