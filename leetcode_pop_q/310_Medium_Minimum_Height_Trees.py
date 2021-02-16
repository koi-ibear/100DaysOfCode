"""
Medium 310. Minimum Height Trees

A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

 

Example 1:


Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.
Example 2:


Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]
Example 3:

Input: n = 1, edges = []
Output: [0]
Example 4:

Input: n = 2, edges = [[0,1]]
Output: [0,1]
"""
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        ## create neighbors map -- use list index trick
        neighbors = [set() for _ in range(n)]
        for i,j in edges:
            neighbors[i].add(j)
            neighbors[j].add(i)
            
        ## find leaves
        leaves = []
        for i,j in enumerate(neighbors):
            if len(j) == 1:
                leaves.append(i)
        nodes_left = n

        ## stop when there are 2 or fewer nodes left
        while nodes_left > 2:
            nodes_left = nodes_left - len(leaves)
            newleaves = []
            ## trim leaves & add new leaves to another layer
            while leaves:
                leaf = leaves.pop()
                nb = neighbors[leaf].pop() # since leaf only has 1 neighbor, fetch it & see if it becomes a leaf
                neighbors[nb].remove(leaf)
                ## if leaf's neighbor becomes leaf, add to newleaves
                if len(neighbors[nb]) == 1:
                    newleaves.append(nb)
            leaves = newleaves
        return leaves

"""
The idea is that we trim out the leaf nodes layer by layer, until we reach the core of the graph, which are the centroids nodes.
Once we trim out the first layer of the leaf nodes (nodes that have only one connection), some of the non-leaf nodes would become leaf nodes.\
"""