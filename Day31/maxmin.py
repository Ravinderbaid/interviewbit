class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        if len(A)==2:
            return [0]*2
        A.sort()
        res=[0]*2
        k=0
        for i in range(len(A)//2):
            res[0]+=abs(A[i]-A[-i-1])
            res[1]+=abs(A[i+k]-A[i+k+1])
            k+=1
            
        res[0] %= 1000000007
        res[1] %= 1000000007
        return res
        

