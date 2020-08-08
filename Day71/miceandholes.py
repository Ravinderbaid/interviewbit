class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def mice(self, A, B):
        A.sort()
        B.sort()
        max1 = 0
        for i in range(len(A)):
            max1 = max(max1, abs(A[i] - B[i]))
        return max1
