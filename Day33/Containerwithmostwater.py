class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArea(self, A):
        left = 0
        r = len(A) - 1
        area = 0
        while left < r:
            area = max(area, (min(A[left], A[r]) * (r - left)))
            if A[left] < A[r]:
                left += 1
            else:
                r -= 1
        return area
