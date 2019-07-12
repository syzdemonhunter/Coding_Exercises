# T: O(n*d)
# S: O(n)

def minNumberOfCoinsForChange(n, denoms):
	if n == 0:
		return 0
    if not denoms or len(denoms) == 0:
    	return -1

    dp = [0]*(n + 1)
    for i in range(1, n + 1):
    	min_val = float('inf')
    	for j in range(len(denoms)):
    		if i >= denoms[j] and dp[i - denoms[j]] != -1:
    			min_val = min(min_val, dp[i - denoms[j]] + 1)

    	dp[i] = -1 if min_val == float('inf') else min_val

    return dp[n]
