"""
Medium 670. Maximum Swap

You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.


Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.
 

Constraints:
"""
class Solution:
    def maximumSwap(self, num: int) -> int:
        s = str(num)
        for i,j in enumerate(s):
            rmax = lmin = j
            rind = lind = i
            for r in range(len(s)-1, i, -1):
                if s[r] > rmax:
                    rmax = s[r]
                    rind = r
            for l in range(0, i+1):
                if s[l] <= lmin:
                    lmin = s[l]
                    lind = l
            if rmax > lmin:
                return s[0:lind]+rmax+s[lind+1:rind]+lmin+s[rind+1:]
        return num