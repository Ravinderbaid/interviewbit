class Solution:
	# @param A : list of strings
	# @return an integer
	def solve(self, A):
	    A=[float(i) for i in A]
	    a=A[0]
	    b=A[1]
	    c=A[2]
	    
	    for i in range(3,len(A)):
	        if 1<(a+b+c)<2:
	            return 1
	        n=A[i]
	        if (a+b+c)>=2:
	            if a>b and a>c:
	                a=n
	            elif b>c:
	                b=n
	            else:
	                c=n
	        else:
	            if a<b and a<c:
	                a=n
	            elif b<c:
	                b=n
	            else:
	                c=n
	    
	    if 1<(a+b+c)<2:
	        return 1
	       
	    return 0 
	                

