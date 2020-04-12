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
?????????
class Solution:
    def shortestWay(self, target, source):
        i, j, n, m = 0, 0, len(source), len(target)
        n_sub = 0
        j = 0
        while j < m:
            max_sub = 0
            cur_sub = 0
            while i < n:
                if source[i] == target[j]:
                    cur_sub += 1
                else:
                    cur_sub = 0
                max_sub = max(max_sub, cur_sub)
                print(max_sub)
                i+=1
            if i ==n and max_sub == 0:
                return -1
            j+= max_sub
            n_sub += 1
        return n_sub


s = Solution()
s.shortestWay('zaza','baz')
