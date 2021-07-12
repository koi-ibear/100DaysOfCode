"""
Medium 417. Pacific Atlantic Water Flow

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.


Example 1:
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Example 2:

Input: heights = [[2,1],[1,2]]
Output: [[0,0],[0,1],[1,0],[1,1]]
"""
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]: return
        m, n = len(heights), len(heights[0])
        p_visited = set()
        a_visited = set()
        
        def dfs(i, j, visited):
            if (i,j) in visited:
                return
            visited.add((i,j))
            for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
                next_i, next_j = i+di, j+dj
                if 0 <= next_i < m and 0 <= next_j < n and heights[next_i][next_j] >= heights[i][j]:
                    dfs(next_i, next_j, visited)

        for i in range(m):
            dfs(i, 0, p_visited)
            dfs(i, n-1, a_visited)
        
        for j in range(n):
            dfs(0, j, p_visited)
            dfs(m-1, j, a_visited)
        
        return list(p_visited & a_visited)
        
        