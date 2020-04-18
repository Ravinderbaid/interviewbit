class Solution:
	# @param A : list of integers
	# @return an integer
	def solve(self, A):
	    max=0
	    min=0
	    
	    n=len(A)
	    A.sort()
	    for i in range(n):
	        min=(min*2)%1000000007
	        min=(min+A[i])%1000000007
	        
	    for i in range(n-1,-1,-1):
	        max=(max*2)%1000000007
	        max=(max+A[i])%1000000007
	        
	    return ((max-min+1000000007)%1000000007)

