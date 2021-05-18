"""
Medium 96. Unique Binary Search Trees

Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

Example 1:


Input: n = 3
Output: 5
Example 2:

Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 19
"""
class Solution:
    def numTrees(self, n: int) -> int:
        """
        G(n): num BST given n nodes
        F(i, n): num BST given i as root with n nodes
        G(n) = F(1, n)+...+F(n,n)
        F(i, n) = G(i-1)*G(n-i)
        """
        if n == 0: return 0
        G = [0]*(n+1)
        G[0] = G[1] = 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                G[i] += G[j-1]*G[i-j]
        return G[-1]
    