"""
Medium 767. Reorganize String


Given a string s, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""
Note:

s will consist of lowercase letters and have length in range [1, 500].
 
"""
class Solution:
    def reorganizeString(self, s: str) -> str:
        res = ''
        ct = Counter(s)
        q = [(-j,i) for i,j in ct.items()]
        heapq.heapify(q)
        pv = 0
        pi = ''
        while q:
            v,i = heapq.heappop(q)
            res += i
            if pv+1 < 0:
                heapq.heappush(q, (pv+1, pi))
            pv, pi = v, i
        if len(res) < len(s):
            return ''
        return res

"""
use heap to save freq
use pv, pi as temp "cool-down" space

if able to use up all letters in s, return s, otherwise it's impossible
"""