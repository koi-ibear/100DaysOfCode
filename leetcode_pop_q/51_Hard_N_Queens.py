"""
Hard 51. N-Queens

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

Example 1:


Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]
"""
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def dfs(queens, xy_diff, xy_tot):
            ## update tracker
            nq = len(queens)
            ## check if tracker meets success criteria -- add to result and exit
            if nq == n:
                result.append(queens)
                return
            ## backtracking -- for each n+1
            for i in range(n):
                ## check if n+1 is valid (not in same column, not on diagonal)
                if i not in queens and nq-i not in xy_diff and nq+i not in xy_tot:
                    ## recursion with updated params
                    dfs(queens+[i], xy_diff+[nq-i], xy_tot+[nq+i])
        
        result = []
        dfs([], [], [])
        return [["."*i+"Q"+"."*(n-i-1) for i in r] for r in result]
    