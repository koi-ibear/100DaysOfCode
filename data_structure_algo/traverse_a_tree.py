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

## Max Depth
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

## Symmetric Tree
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)

    def isMirror(self, tr1, tr2):
        if (tr1==None) and (tr2==None):
            return True
        if (tr1==None) or (tr2==None):
            return False
        return tr1.val == tr2.val and self.isMirror(tr1.left, tr2.right) and self.isMirror(tr1.right, tr2.left)


## Path Sum
#Solution I
class Solution:
    def addition(self, node, tot, sum, res):
        tot = tot + node.val
        if not (node.left or node.right):
            res.append(tot == sum)
        else:
            if node.left:
                self.addition(node.left, tot, sum, res)
            if node.right:
                self.addition(node.right, tot, sum, res)
            
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        tot = 0
        res = []
        self.addition(root, tot, sum, res)
        return any(res)

#Solution II
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if root.val == sum and root.left == None and root.right == None:
            return True
        sum -= root.val
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)