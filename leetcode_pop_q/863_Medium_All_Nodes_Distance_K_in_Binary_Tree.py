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
class Solution2:
    
    def buildParentMap(self, node, parent, parentMap):
        if node is None:
            return
        parentMap[node] = parent
        self.buildParentMap(node.left, node, parentMap)
        self.buildParentMap(node.right, node, parentMap)
        
        
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        # node: parent
        parentMap = {}
        
        # DFS to build the map that maps a node to its parent.
        self.buildParentMap(root, None, parentMap)
       
        # keep the records, since the graph is all connected
        visited = set()
        # results
        ans = []
       
        # Again, DFS to retrieve the nodes within the given distance
        #  this time with the help of the parentMap.
        # Starting from the target node
        def dfs(node, distance):
            if node is None or node in visited:
                return
            
            visited.add(node)
            
            if distance == K:
                ans.append(node.val)
            elif distance < K:
                dfs(node.left, distance+1)
                dfs(node.right, distance+1)
                dfs(parentMap[node], distance+1)
            # else exceed the scope, no need to explore further
        
        dfs(target, 0)
        
        return ans