"""
Medium 261. Graph Valid Tree

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example
Example 1:

Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output: true.
Example 2:

Input: n = 5 edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
Output: false.
"""
class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here
        neighbors = [[] for i in range(n)]
        for i,j in edges:
            neighbors[i].append(j)
            neighbors[j].append(i)
        visited = set()
        q = [0]
        while q:
            cur = q.pop(0)
            if cur in visited:
                return False
            visited.add(cur)
            for nb in neighbors[cur]:
                if nb not in visited:
                    q.append(nb)
        if len(visited) == n:
            return True
        return False