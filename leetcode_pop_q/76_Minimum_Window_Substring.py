"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start = end = 0
        t_dict = dict(Counter(t))
        uniq_t = len(t_dict)
        tracker = {}
        check = 0
        ans = float("inf"), None, None

        while end < len(s):
            if s[end] in t_dict:
                tracker[s[end]] = tracker.get(s[end], 0) + 1
                if tracker[s[end]] == t_dict[s[end]]:
                    check += 1
            while check == uniq_t and start <= end:
                val = s[start]
                # Save the smallest window until now.
                if end - start + 1 < ans[0]:
                    ans = (end - start + 1, start, end)

                if val in tracker:
                    tracker[val] = tracker.get(val, 0) - 1
                    if tracker[val] < t_dict[val]:
                        check -= 1
                # if end - start + 1 < ans[0]:
                #     res = s[start:end+1]
                start += 1
            end += 1
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]

"""
💬
sliding window formula

start = end = 0
init criteria
init answer

while end < len(s):
    {calculate criteria}
    while criteria meets:
        {update answer}
        {recalculate criteria (what happens when start moves right)}
        start += 1
    end += 1

"""