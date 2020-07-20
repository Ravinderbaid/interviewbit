class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        i = 0
        j = len(A) - 1
        c = 0
        while i <= j:
            if A[i] * A[j] < B:
                c += ((j - i) * 2) + 1
                i += 1
            else:
                j -= 1
        return c % (10 ** 9 + 7)
