class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        ans=0
        for i in range(1,A//2+1):
            if not (A-i)%i:
                ans+=1
        return ans
                

