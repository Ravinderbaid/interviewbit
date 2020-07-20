class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        i = 0
        j = len(B) - 1
        closest = 10 ** 9
        pair = []
        while i < len(A) and j >= 0:
            s = abs(A[i] + B[j] - C)
            if s <= closest:
                if s == closest:
                    if A[i] < pair[0]:
                        pair = [A[i], B[j]]
                    elif A[i] == pair[0] and B[j] < pair[1]:
                        pair = [A[i], B[j]]
                else:
                    closest = s
                    pair = [A[i], B[j]]

            if A[i] + B[j] > C:
                j -= 1
            else:
                i += 1
        return pair
