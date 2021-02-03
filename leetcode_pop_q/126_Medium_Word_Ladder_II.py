"""
Hard 126. Word Ladder II

Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        layer = collection.defaultdict()
        layer[beginWord] = [[beginWord]]
        res = []
        wordList = set(wordList)
        wordLen = len(beginWord)
        while layer:
            newlayer = collection.defaultdict()
            for w in layer:
                if w == endWord:
                    res.extend(i for i in layer[w])
                for i in range(wordLen):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        newW = w[:i] + j + w[i+1:]
                        if newW in wordList:
                            wordList[newW] += [layer[w]+[newW]]
            wordList -= set(layer.keys())
        return res

# class Solution:
#     def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
#         wordLen = len(beginWord)
#         wordList = set(wordList)
#         q = collections.deque()
#         q.appendleft((beginWord, [beginWord], 1))
#         ans = []
#         curSet = set()
#         last_len = 0
#         while q:
#             # print(q)
#             curWord, curList, curLen = q.pop()
#             if curLen > last_len:
#                 wordList = wordList - curSet
#                 curSet = set()
#                 if ans:
#                     return ans
#             if curWord == endWord:
#                 ans.append(curList)
#             for i in range(wordLen):
#                 for j in 'abcdefghijklmnopqrstuvwxyz':
#                     newW = curWord[:i]+j+curWord[i+1:]
#                     if newW in wordList:
#                         q.appendleft((newW, curList+[newW], curLen+1))
#                         curSet.add(newW)
#             last_len = curLen
#         return ans
            
"""
starting point:
use traditional data structure for bfs -- queue
return res once answer is found for same length seqs
and also remove visited word so it's efficient for big wordlist
but to find all paths, we can't remove a word once visiting it because it could be useful for other seq
-- we have to remove visited word after same length seq is visited

improvement:
use dictionary instead of queue: {tail_word: [preceding seq]}
iterate on each tail_word each turn (just like queue.pop())
and append to newdict if madeup-new-word is in lookup list

by the end of dict search, assign newdict to dict and start over
until ans is found
"""