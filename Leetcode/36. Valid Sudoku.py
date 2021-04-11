from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """[summary]
        Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
        1. Each row must contain the digits 1-9 without repetition.
        2. Each column must contain the digits 1-9 without repetition.
        3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

        Note:
        A Sudoku board (partially filled) could be valid but is not necessarily solvable.
        Only the filled cells need to be validated according to the mentioned rules.

        Args:
            board (List[List[str]]): board.length == 9, board[i].length == 9, board[i][j] is a digit or '.'.

        Returns:
            bool: Determine if Sudoku board is valid.

        Result:
            Runtime: 80 ms, faster than 99.68% of Python3 online submissions for Valid Sudoku.
            Memory Usage: 14.2 MB, less than 71.49% of Python3 online submissions for Valid Sudoku.
        """

        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        mMat = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):
                cur = board[i][j]
                if cur != '.':
                    k = (i // 3) * 3 + j // 3

                    if cur not in rows[i]:
                        rows[i].add(cur)
                    else:
                        return False

                    if cur not in cols[j]:
                        cols[j].add(cur)
                    else:
                        return False

                    if cur not in mMat[k]:
                        mMat[k].add(cur)
                    else:
                        return False

        return True
