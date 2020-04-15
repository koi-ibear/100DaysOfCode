## Pre-order Traverse
# recursion
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.helper(root, res)
        return res

    def helper(self, node, res):
        if node:
            res.append(node.val)
            self.helper(node.left, res)
            self.helper(node.right, res)

## stack
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res
        


## In-order Traverse
# recursion
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.helper(root, res)
        return res

    def helper(self, node, res):
        if node:
            self.helper(node.left, res)
            res.append(node.val)
            self.helper(node.right, res)

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right

## Post-order Traverse
## recursion
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.helper(root, res)
        return res
        
    def helper(self, node, res):
        if node:
            self.helper(node.left, res)
            self.helper(node.right, res)
            res.append(node.val)

            
## stack
class Solution:
    def postorderTraversal(self, root):
        res, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return res[::-1]




## Level Order Traversal
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        nodes = [root]
        while nodes:
            res.append([n.val for n in nodes])
            nodes = [m for p in [(n.left, n.right) for n in nodes] for m in p if m]
        return res
