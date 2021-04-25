"""
Medium 5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),

"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        slen = len(s)
        if slen==0: return ''
        max_res = 1
        max_sub = s[0]
        
        
        def max_pal(l, r):
            while l >= 0 and r <= slen-1 and s[l] == s[r]:
                l -= 1
                r += 1
            return r-l, s[l+1:r]
        for i in range(slen-1):
            opt1 = max_pal(i,i)
            opt2 = max_pal(i, i+1)
            if opt1[0] > opt2[0]:
                cur_max = opt1[0]
                cur_sub = opt1[1]
            else:
                cur_max = opt2[0]
                cur_sub = opt2[1]
            if cur_max > max_res:
                max_res = cur_max
                max_sub = cur_sub
        return max_sub