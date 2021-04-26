"""
Hard 32. Longest Valid Parentheses

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.

"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        dynamic programming.
        in dp hash, use index associated with ")" to track complete pairs.
        there are two case:
        1. i-1, i are "()": dp[i] = dp[i-2]+2
        2. i-1, i are "))": need to find the beginning of first ")" and check
        if there's a "(" to complete second ")"
            if True:
                dp[i-dp[i-1]-2] (completed pairs before "(")
                + dp[i-1] (complete pairs inner)
                + 2 (wrapper)
            otherwise:
                keep dp[0] = 0 to cutoff connection with downstream
        """
        len_s = len(s)
        if len_s == 0: return 0
        len_tracker = {i: 0 for i in range(len_s)}
        for i in range(len_s):
            if s[i] == ')' and i > 0 and s[i-1] == '(':
                len_tracker[i] = len_tracker.get(i-2, 0)+2
            elif s[i] == ')' and i > 0 and s[i-1] == ')':
                if i - len_tracker[i-1] - 1 >= 0 and s[i - len_tracker[i-1] - 1] == '(':
                    len_tracker[i] = len_tracker[i-1] + len_tracker.get(i - len_tracker[i-1] - 2, 0) + 2
        return max(len_tracker.values())
    
    def longestValidParentheses(self, s: str) -> int:
        """
        stack
        insert one element to stack when see "("
        pop when see ")"
        use last element in stack (incomplete "(" to track completed pairs so far)

        note: need to make sure stack always has at least 2 elements to pop & track
        """
        ans = 0
        stack = [0]
        for i in s:
            if i == '(':
                stack.append(0)
            else:
                if len(stack)>1:
                    p = stack.pop() + 2
                    stack[-1] += p
                    ans = max(ans, stack[-1])
                else:
                    stack = [0]
        return ans


