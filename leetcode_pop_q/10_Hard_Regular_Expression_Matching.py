## UNFINISHED
"""
Hard 10. Regular Expression Matching

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*' where: 

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).


Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input: s = "aab", p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input: s = "mississippi", p = "mis*is*p*."
Output: false
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def scan(s, p, px, pl): # current str, pattern, curent index in pattern
            print(s, p, px)
            if s == '':
                if (px==pl or p[-1] =='*' and px+2==pl): # [finish check] if nothing left on s return True
                    return True
                if px + 2 < pl:
                    return scan(s, p, px+2, pl)
            else:
                res = False
                if px < pl and (s[0] == p[px] or p[px] == '.'):
                    res = res or scan(s[1:], p, px+1, pl)
                    
                    if px +1 < pl and p[px+1] == '*':
                        res = res or scan(s[1:], p, px+2, pl)
                if px < pl and p[px] == '*':
                    if (p[px-1] == s[0] or p[px-1] == '.'):
                        res = res or scan(s[1:], p, px, pl)
                        res = res or scan(s[1:], p, px+1, pl)
                    elif px + 1 < pl:
                        res = res or scan(s, p, px+1, pl)
                        # res = res or scan(s[1:], p, px+1, pl)
                if px < pl -2 and p[px+1] == '*':
                    res = res or scan(s, p, px+2, pl)
                return res
        pl = len(p)
        return scan(s, p, 0, pl)
    
    
    
"""
logic:
if strict / dot match
    move both pointers forward
if *
    if s[0] == pattern[px-1], move s pointer forward or move pattern +2 or move both forward
    else, move pattern pointer forward
if pattern[px+1] *
    move pattern +2
""" 