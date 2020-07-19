class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        list_l = [0] * (max(A) + 1)
        for i in A:
            list_l[i] += 1

        return max(list_l)
