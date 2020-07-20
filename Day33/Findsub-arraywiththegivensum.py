class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        prefix_arr = [A[0]]
        for i in A[1:]:
            prefix_arr.append(prefix_arr[-1] + i)
        i = 0
        j = 0
        flag = False
        while i < len(A) and j < len(A):
            p = prefix_arr[j]
            if flag:
                p -= prefix_arr[i - 1]
            if p == B:
                if i == j:
                    return [A[i]]
                else:
                    return A[i : j + 1]
            elif p < B:
                j += 1
            else:
                flag = True
                i += 1
        return [-1]
