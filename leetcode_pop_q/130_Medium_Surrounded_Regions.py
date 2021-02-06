"""
Medium 130. Surrounded Regions

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""
class Solution:
    """bfs"""
    def solve(self, board: List[List[str]]) -> None:
        if not board: return []
        q = collections.deque()
        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            for j in range(cols):
                if i in [0, rows-1] or j in [0, cols-1]:
                    q.append((i,j))
        while q:
            i, j = q.popleft()
            if 0 <= i < rows and 0 <= j < cols and board[i][j] == 'O':
                board[i][j] = '*'
                q.extend([(i-1, j), (i+1, j), (i, j-1), (i, j+1)])
                
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '*':
                    board[i][j] = 'O'
                    


class Solution:
    """dfs"""
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board: return []
        rows = len(board)
        cols = len(board[0])
        
        def dfs(x,y):
            """
            we only want to flip surrounded Os, so
            flip boarder 0s to *s so that they're not flipped later
            """
            if 0 <= x < rows and 0 <= y < cols and board[x][y] == 'O':
                board[x][y] = '*'
                dfs(x-1, y)
                dfs(x, y-1)
                dfs(x+1, y)
                dfs(x, y+1)
        ## flip Os on upper/lower edge to *sx
        for i in [0, rows-1]:
            for j in range(cols):
                dfs(i, j)
        for i in range(rows):
            for j in [0, cols-1]:
                dfs(i, j)
        
        ## flip Os to Xs and *s to Os
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '*':
                    board[i][j] = 'O'
        return board