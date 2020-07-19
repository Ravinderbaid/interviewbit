class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        if sum(A) == 0:
            return str(0)
        A = sorted(A, key=self.comp(self.compare))
        result = "".join([str(i) for i in A])
        return result

    def compare(self, a, b):
        ab = str(a) + str(b)
        ba = str(b) + str(a)

        return (int(ba) > int(ab)) - (int(ba) < int(ab))

    def comp(self, compare):
        class K(object):
            def __init__(self, obj, *args):
                self.obj = obj

            def __lt__(self, other):
                return compare(self.obj, other.obj) < 0

            def __gt__(self, other):
                return compare(self.obj, other.obj) > 0

            def __eq__(self, other):
                return compare(self.obj, other.obj) == 0

            def __le__(self, other):
                return compare(self.obj, other.obj) <= 0

            def __ge__(self, other):
                return compare(self.obj, other.obj) >= 0

            def __ne__(self, other):
                return compare(self.obj, other.obj) != 0

        return K
