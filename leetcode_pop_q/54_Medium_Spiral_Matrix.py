"""
Medium 54. Spiral Matrix

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        row_begin, col_begin, row_end, col_end = 0, 0, len(matrix), len(matrix[0])
        while row_begin < row_end and col_begin < col_end:
            for i in range(col_begin, col_end):
                ans.append(matrix[row_begin][i])
            row_begin += 1
            for i in range(row_begin, row_end):
                ans.append(matrix[i][col_end-1])
            col_end -= 1
            if row_begin < row_end:
                for i in range(col_end-1, col_begin-1, -1):
                    ans.append(matrix[row_end-1][i])
                row_end -= 1
            if col_begin < col_end:
                for i in range(row_end-1, row_begin-1, -1):
                    ans.append(matrix[i][col_begin])
                col_begin += 1
        return ans
                