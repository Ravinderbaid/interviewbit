class Solution:
    # @param A : list of integers
    # @return an integer
    def bulbs(self, A):
        press = 0
        for i in range(len(A)):
            if press % 2:
                if A[i] == 0:
                    continue
                else:
                    press += 1
            else:
                if A[i] == 1:
                    continue
                else:
                    press += 1

        return press
