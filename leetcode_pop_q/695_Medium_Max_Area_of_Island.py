"""
Medium 695. Max Area of Island

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.

"""
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        def findIsland(x, y, nrow, ncol):
            if x >= nrow or y >= ncol or x < 0 or y < 0 or grid[x][y] != 1:
                return 0
            else:
                area = 1
                grid[x][y] = '*'
                area += findIsland(x+1, y, nrow, ncol)
                area += findIsland(x, y+1, nrow, ncol)
                area += findIsland(x-1, y, nrow, ncol)
                area += findIsland(x, y-1, nrow, ncol)
                return area
        
        nrow = len(grid)
        ncol = len(grid[0])
        max_area = 0
        for r in range(nrow):
            for c in range(ncol):
                res = findIsland(r,c, nrow, ncol)
                if res > max_area:
                    max_area = res
        return max_area
"""
"island area" problem 
-- solution 1 recursive dfs --
def dfs(x, y):
    ## check validity
    if out of bound or not "land":
        return 0 (skip)
    else:
        grid[x][y] = '*' # mark current land as done to save future visit time
        return 1 + dfs(x-1, y) + dfs(x, y-1) + dfs(x+1, y) + dfs(x, y+1) # visit 4 directions until meet "water"

"""