"""
Medium 395. Longest Substring with At Least K Repeating Characters

Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.

Example 1:

Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
"""
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        """
        2. divide & conquer
        """
        if len(s) < k: return 0
        from collections import Counter
        cnt = Counter(s)
        lessthan = [i for i,j in cnt.items() if j<k]
        if not lessthan:
            return len(s)
        mid = -1
        for i,j in enumerate(s):
            if j in lessthan:
                mid = i
                break
        return max(self.longestSubstring(s[0:mid], k), self.longestSubstring(s[mid+1::], k))
        
        
    # def longestSubstring(self, s: str, k: int) -> int:
        # """
        # 1. brute force -- time out
        # """
        # from collections import Counter
        # ls = len(s)
        # ans = []
        # for i in range(ls):
        #     for j in range(i+1, ls+1):
        #         cnt = Counter(s[i:j])
        #         lessthan = 0
        #         for m in cnt:
        #             if cnt[m] < k:
        #                 lessthan += 1
        #                 break
        #         if lessthan == 0:
        #             ans.append(j-i)
        # return max(ans) if ans else 0