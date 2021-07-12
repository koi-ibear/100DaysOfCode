"""
Medium 200. Number of Islands

Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.


Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        if not grid:
            return 0
        self.rows = len(grid)
        self.cols = len(grid[0])
        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    cnt += 1
        return cnt
        
    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= self.rows or j >= self.cols or grid[i][j] != '1':
            return
        else:
            grid[i][j] = '#'
            self.dfs(grid, i-1, j)
            self.dfs(grid, i+1, j)
            self.dfs(grid, i, j-1)
            self.dfs(grid, i, j+1)

class Solution:
    """round 2"""
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return
        m, n = len(grid), len(grid[0])
        
        def dfs(i,j):
            grid[i][j] = 'x'
            for di, dj in [[0,1], [0,-1], [1,0], [-1,0]]:
                if 0 <= i+di < m and 0 <= j+dj < n and grid[i+di][j+dj] == '1':
                    dfs(i+di, j+dj)         
            
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i,j)
                    ans += 1
        return ans    