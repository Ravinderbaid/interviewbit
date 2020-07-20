class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        i = 0
        j = len(A) - 1
        c = 0
        while i < j:
            if A[i] + A[j] == B:
                c += 1
                i += 1
                j -= 1
            elif A[i] + A[j] > B:
                j -= 1
            else:
                i += 1
        return c
