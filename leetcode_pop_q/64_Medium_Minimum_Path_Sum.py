"""
Medium 64. Minimum Path Sum


Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
 

Example 1:


Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 100
"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid: return
        n, m = len(grid[0]), len(grid)
        ans = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                tmp = None
                if i >0 and j > 0:
                    tmp = min(ans[i-1][j], ans[i][j-1])
                elif i == 0:
                    tmp = ans[i][j-1]
                elif j == 0:
                    tmp = ans[i-1][j]
                ans[i][j] = tmp + grid[i][j]
        return ans[-1][-1]