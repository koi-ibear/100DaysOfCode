"""
🌸 Medium 1055. Shortest Way to Form String  
From any string, we can form a subsequence of that string by deleting some number of characters (possibly no deletions).

Given two strings source and target, return the minimum number of subsequences of source such that their concatenation equals target. If the task is impossible, return -1

Example 1:

Input: a="zaza", b="baz"
Output: 3
Explanation:
copy1="z"
copy2="az"
copy3="a
a=copy1+copy2+copy3
"""

class Solution:
    def shortestWay(self, target, source):
        t, s, m, n = 0, 0, len(target), len(source)
        n_substr = 0
        while t < m:
            t1 = t
            max_sub = 0
            s = 0
            while s < n and t1 < m:
                if target[t1] == source[s]:
                    t1+=1 # move temp_t pointer to trace cur substr
                else:
                    max_sub = max(max_sub, t1-t)
                    t1 = t
                s += 1 # s moves forward regardless, so add outside if condition
            max_sub = max(max_sub, t1-t)
            if max_sub==0:
                return -1
            t+= max_sub
            n_substr+=1
        return n_substr