"""
Medium 791. Custom Sort String

order and str are strings composed of lowercase letters. In order, no letter occurs more than once.

order was sorted in some custom order previously. We want to permute the characters of str so that they match the order that order was sorted. More specifically, if x occurs before y in order, then x should occur before y in the returned string.

Return any permutation of str (as a string) that satisfies this property.

Example:
Input: 
order = "cba"
str = "abcd"
Output: "cbad"
Explanation: 
"a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a". 
Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.
"""
class Solution:
    def customSortString(self, order: str, str: str) -> str:
        cnt = {}
        for i in str:
            cnt[i] = cnt.get(i, 0) + 1
        ans = ''
        for i in order:
            if i not in cnt: continue
            ans += i * cnt[i]
            cnt.pop(i)
        for i in cnt:
            ans += cnt[i] * i
        return ans