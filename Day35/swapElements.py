class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        Ad=list(A)
        n=len(A)
        mxi=max(A)
        for i in range(1,n+1):
            mx=Ad[i-1]
            for j in range(i,n+1,i):
                Ad[j-1]=max(Ad[j-1],A[i-1])
                mx=max(mx,A[j-1])
            Ad[i-1]=mx
        ans=[]
        for q in B:
            if q[1]==0:
                ans.append(A[q[0]-1])
            elif q[1]==1:
                ans.append(Ad[q[0]-1])
            else:
                ans.append(mxi)
        return ans
