"""
Medium 113. Path Sum II

Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where each path's sum equals targetSum.

A leaf is a node with no children.

 

Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: []
Example 3:

Input: root = [1,2], targetSum = 0
Output: []
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root: return []
        ans = []
        def findTrace(trace, node, target):
            if target == node.val and not node.left and not node.right:
                trace = trace + [node.val]
                ans.append(trace)
            if node.left:
                findTrace(trace+[node.val], node.left, target-node.val)
            if node.right:
                findTrace(trace+[node.val], node.right, target-node.val)
        findTrace([], root, targetSum)
        return ans