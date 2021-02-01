"""
Medium 103. Binary Tree Zigzag Level Order Traversal

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]
"""
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        from collections import deque
        queue = deque()
        ans = []
        queue.append(root)
        l2r = False
        while queue:
            tmp = []
            num_nodes = len(queue)
            for i in range(num_nodes):
                
                if l2r:
                    cur = queue.pop()
                    if cur.right:
                        queue.appendleft(cur.right)
                    if cur.left:
                        queue.appendleft(cur.left)
                else:
                    cur = queue.popleft()
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)
                tmp.append(cur.val)
            ans.append(tmp)
            l2r = 1- l2r
        return ans      
        