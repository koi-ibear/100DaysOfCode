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



## Count Univalue Subtrees
class Solution:
    def countUnivalSubtrees(self, root):
        self.count = 0
        self.helper(root)
        return self.count
    def helper(self, node):
        if not node:
            return False
        if not node.left and not node.right:
            self.count += 1
            return True
        uni = True
        if node.left:
            uni = uni and self.helper(node.left) and node.val == node.left.val
        if node.right:
            uni = uni and self.helper(node.right) and node.val == node.right.val
        self.count += uni
        return uni  


## Construct Binary Tree from Inorder and Postorder Traversal
class Solution:
    def linkNode(self, start, end):
        if start > end:
            return None
        root = self.postorder.pop()
        node = TreeNode(root)
        ind = self.inorder_index[node.val]
        node.right = self.linkNode(ind+1, end)
        node.left= self.linkNode(start, ind-1)
        return node
        
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        self.inorder_index = {j:i for i,j in enumerate(inorder)}
        self.inorder = inorder
        self.postorder = postorder
        if not self.inorder or not self.postorder:
            return None
        return self.linkNode(0, len(postorder)-1)

"""
💬
1. features of tree:
    1.1. postorder last element is root, 
    1.2. left and right to which in inorder are left & right nodes;
2. as for stop rule, always think of base case: what if there's only 1 node in this tree
"""

## Construct Binary Tree from Preorder and Inorder Traversal
class Solution:
    def helper(self, start, end):
        if start > end:
            return None
        node = TreeNode(self.preorder.pop(0))
        in_idx = self.inorder_map[node.val]
        node.left = self.helper(start, in_idx-1)
        node.right = self.helper(in_idx+1, end)
        return node
        
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        self.preorder = preorder
        self.inorder = inorder
        self.inorder_map = {j: i for i,j in enumerate(self.inorder)}
        return self.helper(0, len(inorder)-1)


## Populating Next Right Pointers in Each Node
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        cur = root
        next_ = cur.left
        while next_:
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left
                cur = cur.next
            else:
                cur = next_
                next_ = cur.left
