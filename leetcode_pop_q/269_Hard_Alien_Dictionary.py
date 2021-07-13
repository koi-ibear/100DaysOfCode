"""
Hard 269. Alien Dictionary

Description
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

You may assume all letters are in lowercase.
The dictionary is invalid, if a is prefix of b and b is appear before a.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return the smallest in normal lexicographical order
Example
Example 1:

Input：["wrt","wrf","er","ett","rftt"]
Output："wertf"
Explanation：
from "wrt"and"wrf" ,we can get 't'<'f'
from "wrt"and"er" ,we can get 'w'<'e'
from "er"and"ett" ,we can get 'r'<'t'
from "ett"and"rftt" ,we can get 'e'<'r'
So return "wertf"
Example 2:

Input：["z","x"]
Output："zx"
Explanation：
from "z" and "x"，we can get 'z' < 'x'
So return "zx"
"""

from heapq import *
class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        # Write your code here
        small_large_pair = {ch:[] for word in words for ch in word}
        degrees = {ch:0 for word in words for ch in word}
        for i in range(len(words)-1):
            len0, len1 = len(words[i]), len(words[i+1])
            maxlen = min(len0, len1)
            for j in range(maxlen):
                if words[i][j] == words[i+1][j]:
                    if j == maxlen-1 and len0 > len1:
                        return ""
                    continue
                degrees[words[i+1][j]] += 1
                small_large_pair[words[i][j]].append(words[i+1][j])
                break
            
        print(degrees)
        print(small_large_pair)
        ## {'a': ['b', 'c,' 'd'], "c": ['d']} -> ['a','b','c','d']
        ans = []
        degree0 = [i for i,j in degrees.items() if j == 0]
        heapify(degree0)
        while degree0:
            ch = heappop(degree0)
            ans.append(ch)
            for nb in small_large_pair[ch]:
                degrees[nb] -= 1
                if degrees[nb] == 0:
                    heappush(degree0, nb)
        if len(ans)!=len(degrees): return ""
        return "".join(ans)