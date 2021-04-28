"""
Hard 72. Edit Distance


Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""

class Solution:
    """
    recursion
    """
    def minDistance(self, word1: str, word2: str) -> int:
        return self.dfs(word1, word2, 0, 0, {})
        
    def dfs(self, word1, word2, i, j, cache):
        if i == len(word1) and j==len(word2): return 0
        elif i == len(word1): return len(word2)-j
        elif j == len(word2): return len(word1)-i
        
        if (i,j) not in cache:
            if word1[i] == word2[j]:
                ans = self.dfs(word1, word2, i+1, j+1, cache)
            else:
                insert = 1 + self.dfs(word1, word2, i+1, j, cache)
                remove = 1 + self.dfs(word1, word2, i, j+1, cache)
                replace = 1 + self.dfs(word1, word2, i+1, j+1, cache)
                ans = min(insert, remove, replace)
            cache[(i,j)] = ans
        return cache[(i,j)]
        
class Solution:
    """
    iteration
    """
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        tracker = [[0]*(m+1) for i in range(n+1)]
        
        ## initialize first row & column as difference between pointers
        for i in range(m+1):
            tracker[i][0] = i
        for j in range(n+1):
            tracker[0][j] = j
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    tracker[i][j] = tracker[i-1][j-1]
                else:
                    tracker[i][j] = min(tracker[i][j-1], tracker[i-1][j], tracker[i-1][j-1]) +1
        return tracker[-1][-1]


#         a   b    
#     [0  1   2]
# d   [1  1   2]
# b   [2  2   1]
# c   [3  4   2]