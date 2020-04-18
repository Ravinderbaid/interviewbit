class Solution:
	# @param A : list of integers
	# @return an integer
	def solve(self, A):
	    A.sort()
	    MOD = 1000000007
	    min_sum=0
	    max_sum=0
	    n=len(A)
	    for i in range(0,n):
	        
	        max_sum= 2*max_sum+A[n-1-i]
	        max_sum%=MOD
	        min_sum=2*min_sum+A[i]
	        min_sum%=MOD
	        
	    return (max_sum-min_sum+MOD)%MOD

