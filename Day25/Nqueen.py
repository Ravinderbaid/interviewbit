class Solution:
    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, A):
        n=A
        stack, res = [[(0, i)] for i in range(n)], []
        while stack:
            board = stack.pop()
            row = len(board)
            if row == n:
                res.append([''.join('Q' if i == c else '.' for i in range(n))
                            for r, c in board])
            for col in range(n):
                if all(col != c and abs(row-r) != abs(col-c)for r, c in board):
                    stack.append(board+[(row, col)])
        return res
