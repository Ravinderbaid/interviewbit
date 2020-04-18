class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        res=[0]*(A+1)
        for booking in B:
                res[booking[0]-1]+=booking[2]
                res[booking[1]]-=booking[2]
        for i in range(1,A):
            res[i]+=res[i-1]
        res.pop()
        return res

