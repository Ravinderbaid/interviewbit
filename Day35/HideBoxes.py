class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        n = len(A)
        j = n // 2
        i = 0
        ans = n
        while i < n // 2 and j < n:
            if A[i] * 2 <= A[j]:
                ans -= 1
                j += 1
                i += 1
            else:
                j += 1

        return ans
