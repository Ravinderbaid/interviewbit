class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        l=[0]*(max(A)+1)
        for i in A:
            l[i]+=1
            
        return max(l)

