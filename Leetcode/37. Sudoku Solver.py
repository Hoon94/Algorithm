from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """[summary]
        Write a program to solve a Sudoku puzzle by filling the empty cells.
        A sudoku solution must satisfy all of the following rules:
        1. Each of the digits 1-9 must occur exactly once in each row.
        2. Each of the digits 1-9 must occur exactly once in each column.
        3. Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

        Args:
            board (List[List[str]]): board.length == 9, board[i].length == 9, board[i][j] is a digit or '.'.

        Returns:
            It is guaranteed that the input board has only one solution.

        Result:
            Runtime: 2036 ms, faster than 5.02% of Python3 online submissions for Sudoku Solver.
            Memory Usage: 14.3 MB, less than 72.67% of Python3 online submissions for Sudoku Solver.
        """

        self.board = board
        self.solve()

    def findUnassigned(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == '.':
                    return row, col
        return -1, -1

    def solve(self):
        row, col = self.findUnassigned()
        if (row, col) == (-1, -1):
            return True

        for num in map(str, range(1, 10)):
            if self.isSafe(row, col, num):
                self.board[row][col] = num
                if self.solve():
                    return True
                self.board[row][col] = '.'

    def isSafe(self, row, col, ch):
        rowSafe = all(self.board[row][_] != ch for _ in range(9))
        colSafe = all(self.board[_][col] != ch for _ in range(9))
        squareSafe = all(self.board[r][c] != ch for r in self.getRange(
            row) for c in self.getRange(col))
        return rowSafe and colSafe and squareSafe

    def getRange(self, x):
        x -= x % 3
        return range(x, x + 3)
