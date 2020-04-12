"""
🌸 Medium 809. Expressive Words

Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo", "hi" -> "hiiii".  In these strings like "heeellooo", we have groups of adjacent letters that are all the same:  "h", "eee", "ll", "ooo".

For some given string S, a query word is stretchy if it can be made to be equal to S by any number of applications of the following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is 3 or more.

For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has size less than 3.  Also, we could do another extension like "ll" -> "lllll" to get "helllllooo".  If S = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = S.

Given a list of query words, return the number of words that are stretchy. 

 

Example:
Input: 
S = "heeellooo"
words = ["hello", "hi", "helo"]
Output: 1
Explanation: 
We can extend "e" and "o" in the word "hello" to get "heeellooo".
We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.
 

Notes:

0 <= len(S) <= 100.
0 <= len(words) <= 100.
0 <= len(words[i]) <= 100.
S and all words in words consist only of lowercase letters
"""

class Solution:
    def stretchy(self, s, w):
        i, j, i1, j1, n, m = 0, 0, 0, 0, len(s), len(w)
        while i < n and j < m:
            if s[i] != w[j]:
                return False
            while i1 < n and s[i] == s[i1]:
                i1+=1
            while j1 < m and w[j] == w[j1]:
                j1+=1
            if (i1-i) != (j1-j) and i1-i < max(3, j1-j):
                return False
            i = i1
            j = j1
        return i==n and j==m
            
            
    def expressiveWords(self, S: str, words: List[str]) -> int:
        return sum(self.stretchy(S, word) for word in words)

"""
💬 
sliding door type solution. 
keep track of start n end point for each object
update start poin when recurring ends (detected by end point)
"""
