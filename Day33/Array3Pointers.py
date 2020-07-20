class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def minimize(self, A, B, C):
        a = A
        b = B
        c = C
        la = len(a)
        lb = len(b)
        lc = len(c)

        i = j = k = 0
        ans = float("inf")
        result = 0
        while i < la and j < lb and k < lc:
            minimum = min(a[i], b[j], c[k])
            maximum = max(a[i], b[j], c[k])
            if maximum - minimum < ans:
                result = i, j, k
                ans = maximum - minimum
            if ans == 0:
                break
            if a[i] == minimum:
                i += 1
            elif b[j] == minimum:
                j += 1
            else:
                k += 1
        i, j, k = result
        return max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i]))
