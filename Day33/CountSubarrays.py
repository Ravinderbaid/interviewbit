class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        i=0
        j=0
        s = {}
        ans=0
        p=j
        while(i<len(A)):
            while(j<len(A) and s.get(A[j],True)):
                s[A[j]]=False
                j+=1
            ans+=(j-i)
            s.pop(A[i])
            i+=1
            
        return (ans%(10**9+7))
                
