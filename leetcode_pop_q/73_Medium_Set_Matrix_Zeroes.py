"""
Medium 73. Set Matrix Zeroes

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.

You must do it in place.

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
"""
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        2. use matrix to mark 0s
        space O(1)
        time O(N*M)
        """
        nrow, ncol = len(matrix), len(matrix[0])
        col0 = False
        for i in range(nrow):
            if matrix[i][0] == 0:
                col0 = True
            for j in range(1, ncol):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(nrow-1, -1, -1):
            for j in range(ncol-1, 0, -1):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0
            if col0:
                matrix[i][0] = 0
        return matrix
    
    
    # def setZeroes(self, matrix: List[List[int]]) -> None:
    #     """
    #     1. extra space
    #     space O(N+M); tim O(N*M)
    #     Do not return anything, modify matrix in-place instead.
    #     """
    #     nrow, ncol = len(matrix), len(matrix[0])
    #     zero_row = []
    #     zero_col = []
    #     for i in range(nrow):
    #         for j in range(ncol):
    #             if matrix[i][j] == 0:
    #                 zero_row.append(i)
    #                 zero_col.append(j)
    #     for i in zero_row:
    #         for j in range(ncol):
    #             matrix[i][j] = 0
    #     for j in zero_col:
    #         for i in range(nrow):
    #             matrix[i][j] = 0
    #     return matrix