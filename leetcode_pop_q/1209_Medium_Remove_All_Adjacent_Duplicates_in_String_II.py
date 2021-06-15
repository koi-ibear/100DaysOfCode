"""
Medium 1209. Remove All Adjacent Duplicates in String II

You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

 

Example 1:

Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.
Example 2:

Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"
Example 3:

Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"
"""

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        """
        1. stack
        """
        stack = [] #[char, num]
        for i in s:
            if not stack or stack[-1][0] != i:
                stack.append([i, 1])
            elif stack[-1][1] + 1 < k:
                stack[-1][1] += 1
            else:
                stack.pop()
        ans = ''
        for i,j in stack:
            ans+= i*j
        return ans
 
     # def removeDuplicates(self, s: str, k: int) -> str:
     #    """
     #    X 2. recursion --  timeout
     #    """
     #    ls = len(s)
     #    for i in range(ls):
     #        if i+k <= ls and s[i:i+k] == s[i]*k:
     #            return self.removeDuplicates(s[:i]+s[i+k:], k)
     #    return s
        