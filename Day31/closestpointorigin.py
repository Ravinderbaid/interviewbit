class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return a list of list of integers
    def solve(self, A, B):
        A.sort(key=self.Eucled)
        return A[:B]

    def Eucled(self, l):
        return l[0] ** 2 + l[1] ** 2
