"""
Hard 329. Longest Increasing Path in a Matrix

Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

 

Example 1:


Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:


Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
Example 3:

Input: matrix = [[1]]
Output: 1
"""
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        nrow = len(matrix)
        if nrow == 0:
            return 0
        ncol = len(matrix[0])
        tracker = {}
        def findIncreasing(matrix, r, c):
            if (r,c) in tracker:
                return tracker[(r,c)]
            ans = 1
            for (i,j) in [(0,1), (0,-1), (1,0), (-1,0)]:
                if 0 <= r+i < nrow and 0 <= c+j < ncol and matrix[r+i][c+j] > matrix[r][c]:
                    ans = max(ans, 1 + findIncreasing(matrix, r+i, c+j))
                else:
                    ans = max(ans, 1)
            tracker[(r,c)] = ans
            return ans
        
        res = []
        for i in range(nrow):
            for j in range(ncol):
                res.append(findIncreasing(matrix, i, j)) 
        return max(res)