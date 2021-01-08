"""
🌸 Medium 222. Count Complete Tree Nodes

Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
"""

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        """
        in complete binary tree, # nodes = 1 (root) + # left_nodes + # right_nodes
        if left tree is perfect (depth(left) = depth(right)):
          # left_nodes = 2**depth - 1
          # right_nodes = recursively count nodes
        """
        if root is None:
            return 0
        leftDep = self.countDepth(root.left)
        rightDep = self.countDepth(root.right)
        
        if leftDep == rightDep:
            return pow(2, leftDep) - 1 + self.countNodes(root.right) + 1
        else:
            return pow(2, rightDep) - 1 + self.countNodes(root.left) + 1

    def countDepth(self, root):
        """
        since it's a complete tree, depth == left branch depth
        """
        if root is None:
            return 0
        else:
            return self.countDepth(root.left) + 1