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
        ans = []
        
        def placeQ(qy, cur_col, xy_sum, xy_diff):
            # print(qy)
            cur_row = len(qy)
            if cur_row == n:
                if qy not in ans:
                    ans.append(qy)
                return True

            if cur_col not in qy and cur_col + cur_row not in xy_sum and cur_row - cur_col not in xy_diff:
                # qy = qy + (cur_col,)
                # xy_diff.add(cur_row - cur_col)
                cur_row += 1
                for j in range(n):
                    placeQ(qy + (cur_col,), j, xy_sum+[cur_row + cur_col], xy_diff+[cur_row - cur_col])
        
        for i in range(n):
            placeQ(tuple(), i, [], [])
        print(ans)
        return len(ans)
          