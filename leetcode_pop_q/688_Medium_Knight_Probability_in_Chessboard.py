"""
Medium 688. Knight Probability in Chessboard

On an NxN chessboard, a knight starts at the r-th row and c-th column and attempts to make exactly K moves. The rows and columns are 0 indexed, so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).

A chess knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.


Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

The knight continues moving until it has made exactly K moves or has moved off the chessboard. Return the probability that the knight remains on the board after it has stopped moving.

 
Example:

Input: 3, 2, 0, 0
Output: 0.0625
Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.
"""
class Solution:
#     def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
#         def helper(cur_moves, r, c):
#             elig[(r,c)] = elig.get((r,c), 0 <= r < N and 0 <= c < N)
#             if not elig[(r,c)]:
#                 self.fails += 8**(K-cur_moves)
#                 return
#             if cur_moves == K:
#                 self.successes += 1
#                 return
#             helper(cur_moves+1, r+2, c+1)
#             helper(cur_moves+1, r+1, c+2)
#             helper(cur_moves+1, r+2, c-1)
#             helper(cur_moves+1, r+1, c-2)
#             helper(cur_moves+1, r-2, c+1)
#             helper(cur_moves+1, r-1, c+2)
#             helper(cur_moves+1, r-2, c-1)
#             helper(cur_moves+1, r-1, c-2)            
#         self.successes = 0
#         self.fails = 0
#         elig = {}
#         helper(0, r, c)            
#         return self.successes/(self.successes+self.fails)

    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        def helper(cur_moves, r, c):
            if not(0 <= r < N and 0 <= c < N):
                return 0
            if cur_moves == K:
                return 1
            res = 0
            for i,j in [(1,2), (1,-2), (-1,2), (-1,-2),
                       (2,1), (2,-1), (-2,1), (-2,-1)]:
                p = prob.get((cur_moves+1, r+i, c+j))
                if not p:
                    p = helper(cur_moves+1, r+i, c+j)
                    prob[(cur_moves+1, r+i, c+j)] = p
                res += 1/8 * p
            return res
      
        prob = {}
        return helper(0, r, c)            
        