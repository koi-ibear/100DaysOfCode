"""
Medium 542. 01 Matrix

Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

 

Example 1:

Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
Example 2:

Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]
 """
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []
        rows = len(matrix)
        cols = len(matrix[0])
        dist = [[None for _ in range(cols)] for _ in range(rows)]
        # create queue & add all 0s to it
        q = []
        visited = set()
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
                    q.append((i,j))
                    visited.add((i,j))
        step = 0
        while q:
            step += 1
            newq = []
            for (i,j) in q:
                for nb_i, nb_j in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if 0 <= nb_i < rows and 0 <= nb_j < cols and (nb_i, nb_j) not in visited:
                        dist[nb_i][nb_j] = step
                        newq.append((nb_i, nb_j))
                        visited.add((nb_i, nb_j))
            q = newq
        return dist