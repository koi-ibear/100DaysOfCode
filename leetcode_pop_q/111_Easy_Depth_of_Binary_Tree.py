"""
🌸 Easy 111. Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children. 

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        from queue import Queue
        # step 1: check if tree exists
        if root is None:
            return 0
        # step 2: create empty Queue & add root
        q = Queue()
        q.put(root)
        # step 3: use visited to track visited nodes if needed -- not needed for this prob
        # visited = set()
        # step 4: initiate tracker -- depth in this prob
        dpt = 0
        # step 5: if queue is not empty, loop through elements in queue
        while not q.empty():
            size = q.qsize()
            # step 6: loop len(queue) steps for current layer
            for i in range(size):
                # step 7: get current element (FIFO)
                cur = q.get()
                # step 8: check if target found
                if cur.left is None and cur.right is None:
                    return dpt + 1
                # step 9: append children to queue (for next round)
                if cur.left is not None:
                    q.put(cur.left)
                if cur.right is not None:
                    q.put(cur.right)
            # step 10: update tracker
            dpt += 1
        return dpt
            