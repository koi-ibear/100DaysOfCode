"""
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.
"""
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        old | neighbor | action | code
        1 | < 2 or > 3 | 1 -> 0 | 3 (die)
        1 | 2 or 3 | 1 -> 1 | 1 (still live)
        0 | 3 | 0 -> 1 | 2 (rebirth)
        """
        n_row = len(board)
        n_col = len(board[0])
        if n_row * n_col == 0:
            return
        for i, row in enumerate(board):
            for j, ind in enumerate(row):
                nb = sum(1 if board[r][c] in [1, 3] and not (r==i and c==j) else 0 for r in range(max(0, i-1), min(n_row, i+2)) for c in range(max(0, j-1), min(n_col, j+2)))
                if board[i][j]:
                    if nb < 2 or nb > 3:
                        board[i][j] = 3
                else:
                    if nb == 3:
                        board[i][j] = 2
                # print(i, j, nb, [board[r][c] for r in range(max(0, i-1), min(n_row, i+2)) for c in range(max(0, j-1), min(n_col, j+2))])
        for i, row in enumerate(board):
            for j, ind in enumerate(row):
                if board[i][j] == 3:
                    board[i][j] = 0
                if board[i][j] == 2:
                    board[i][j] = 1
        return board
            
"""
💬
1. one way to solve memory O(1) is to create a map (a new value as secret code) updated value and update in another loop"""
