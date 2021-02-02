"""
Hard 127. Word Ladder

A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words such that:

The first word in the sequence is beginWord.
The last word in the sequence is endWord.
Only one letter is different between each adjacent pair of words in the sequence.
Every word in the sequence is in wordList.
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog" with 5 words.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no possible transformation.
 

Constraints:

1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the strings in wordList are unique.
"""
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordsize = len(beginWord)
        wordList = set(wordList)
        from collections import deque
        queue = deque()
        step = 0
        queue.appendleft((beginWord, 1))
        while queue:
            cur, curlen = queue.pop()
            if cur == endWord:
                return curlen
            for i in 'abcdefghijklmnopqrstuvwxyz':
                for j in range(0, wordsize):
                    tmp = cur[0:j]+i+cur[j+1:]
                    if tmp in wordList:
                        queue.appendleft((tmp, curlen+1))
                        wordList.remove(tmp)
        return 0

"""
Below is first try, which got timeout error

takeaway:
- when the word list is long, it's not efficient to compare word-in-queue with each of the word in list any more
- instead, can "make" new words with 26 letters & check existence in word list
- once add obj in queue, can move it from word list (based on unique criteria)
"""

# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         if len(wordList) == 0 or endWord not in wordList: return 0
        
#         from collections import deque
#         visited = set()
#         word_set = set(wordList)
#         word_set.add(beginWord)
#         def diff_letter(w1, w2):
#             diff = 0
#             for i, (j, k) in enumerate(zip(w1, w2)):
#                 if j != k:
#                     diff += 1
#                 if diff > 1:
#                     return -1
#             return diff # if 2 or more letter diff, return -1; if 1 letter diff, return 1, if same, return 0
        
#         queue = deque()
#         step = 0
#         queue.appendleft(beginWord)
#         while queue:
#             step += 1
#             ql = len(queue)
#             for i in range(ql):
#                 cur = queue.pop()
#                 if cur in visited:
#                     continue
#                 visited.add(cur)
#                 word_set.remove(cur)
#                 if diff_letter(cur, endWord) == 0:
#                     return step
#                 for j in word_set:
#                     if j in visited:
#                         continue
#                     check = diff_letter(cur, j)
#                     if check == 1:
#                         queue.appendleft(j)
#         return 0
       