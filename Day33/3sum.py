class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        A.sort()
        current = 10 ** 8
        for i in range(len(A) - 2):
            p = i + 1
            q = len(A) - 1
            while p < q:
                x = A[p] + A[q] + A[i]
                if abs(B - x) <= abs(B - current):
                    current = x
                if x > B:
                    q -= 1
                else:
                    p += 1
        return current
