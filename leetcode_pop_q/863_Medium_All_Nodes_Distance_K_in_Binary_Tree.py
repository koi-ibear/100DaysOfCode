"""
Medium 863. All Nodes Distance K in Binary Tree

We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.

 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.



Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.
 

Note:

The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.
"""
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        ## annotate parent w. dfs
        def annoParent(node, parent):
            if node:
                node.par = parent
                annoParent(node.left, node)
                annoParent(node.right, node)
        
        annoParent(root, None)
        
        q = collections.deque()
        q.append((target, 0)) # add (target, distance_to_tar) to queue
        seen = set()
        seen.add(target)
        while q:
            # check if reach K
            if q[-1][1] == K:
                return [i[0].val for i in q]
            node, dist = q.pop()
            for nb in (node.left, node.right, node.par):
                if nb and nb not in seen:
                    q.appendleft((nb, dist+1))
                    seen.add(nb)
        return []
            
"""
1. when find "neighbors" in binary tree, we need to know parent node
2. neighbor: left, right, parent
3. use dfs to annotate parent and bfs to find neighbors with certain distance
4. trick: use q[-1] to peek what's the current distance
5. trick: for seen set, add & check both happen when adding new nodes
"""