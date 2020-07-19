class Solution:
    # @param A : list of integers
    # @return a list of integers

    def rightRotate(self, A, outOfPlace, cur):
        temp = A[cur]
        for i in range(cur, outOfPlace, -1):
            A[i] = A[i - 1]

        A[outOfPlace] = temp
        return A

    def solve(self, A):
        outOfPlace = -1
        for i in range(len(A)):
            if outOfPlace >= 0:

                if (A[i] >= 0 and A[outOfPlace] < 0) or (
                    A[i] < 0 and A[outOfPlace] >= 0
                ):
                    A = self.rightRotate(A, outOfPlace, i)
                    if (i - outOfPlace) > 2:
                        outOfPlace += 2
                    else:
                        outOfPlace = -1
            if outOfPlace == -1:
                if (A[i] >= 0 and not i % 2) or (A[i] < 0 and i % 2):
                    outOfPlace = i

        return A
