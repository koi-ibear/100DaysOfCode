"""
Hard 52. N-Queens II

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

 
Example 1:


Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
Example 2:

Input: n = 1
Output: 1

"""
class Solution:
    def totalNQueens(self, n: int) -> int:
        self.ans = 0
        def placeQ(qy, xy_sum, xy_diff):
            # print(qy)
            cur_row = len(qy)
            if cur_row == n:
                self.ans+=1
                return

            for j in range(n):
                if j not in qy and j+cur_row not in xy_sum and cur_row-j not in xy_diff:
                    
                    placeQ(qy + (j,), xy_sum+[cur_row + j], xy_diff+[cur_row - j])
        placeQ(tuple(), [], [])
        return self.ans
