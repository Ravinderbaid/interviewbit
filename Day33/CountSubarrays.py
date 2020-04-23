class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        i=0
        j=0
        s = {}
        ans=0
        while(i<len(A)):
            while(j<len(A) and not s.get(A[j],None)):
                s[A[j]]=1
                j+=1
            ans+=((j-i)*(j-i+1))//2
            s.pop(A[i])
            i+=1
        return (ans%10**9+7)
                
