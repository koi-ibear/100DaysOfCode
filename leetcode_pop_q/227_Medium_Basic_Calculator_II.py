"""
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
"""

class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        sign = '+'
        res = []
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord('0')
            if not s[i].isdigit() and not s[i].isspace() or i==len(s)-1:
                if sign == '+':
                    res.append(num)
                elif sign == '-':
                    res.append(-num)
                elif sign == '*':
                    tmp = res.pop()
                    res.append(tmp*num)
                else:
                    tmp = res.pop()
                    res.append(floor(tmp/num) if tmp / num > 0 else ceil(tmp/num))
                sign = s[i]
                num = 0
        return sum(res)