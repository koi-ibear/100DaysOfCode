"""
Medium 22. Generate Parentheses


Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        nl = n
        nr = n
        ans = set()
        def pair(nl, nr, seq):
            if seq in ans or nl < 0 or nr < 0 or nl > nr: # [validity check] if visited before or less than 0 left or more right than left is in seq, return
                return
            if nl == 0 and nr == 0: # [finish check] if both used up, add to ans
                ans.add(seq)
                return
            pair(nl-1, nr, seq+'(')
            pair(nl, nr-1, seq+')')
        pair(n, n, '')
        return ans