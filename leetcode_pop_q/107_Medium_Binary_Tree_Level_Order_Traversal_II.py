"""
Medium 107. Binary Tree Level Order Traversal II

Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
"""
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        q = [root]
        ans = [[root.val]]
        while q:
            tmp = []
            val = []
            for i in q:
                if i.left:
                    tmp.append(i.left)
                    val.append(i.left.val)
                if i.right:
                    tmp.append(i.right)
                    val.append(i.right.val)
            q = tmp
            if val:
                ans.append(val)
        return ans[::-1]
            