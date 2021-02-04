"""
Hard 301. Remove Invalid Parentheses

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
"""
class Solution:
    def valid(self, s):
        cnt = 0
        for c in s:
                if c == '(':
                    cnt += 1
                elif c == ')':
                    cnt -= 1
                if cnt < 0:
                    return False
        if cnt == 0:
            return True
        return False
        
    def removeInvalidParentheses(self, s: str) -> List[str]:
        if s == '':
            return [s]
        ans = []

        found = False
        visited = set()
        q = collections.deque()
        q.appendleft(s)

        while q:
            cur = q.pop()
            if cur in visited:
                continue
            visited.add(cur)
            if self.valid(cur):
                ans.append(cur)
                found = True
            if found:
                continue
            curLen = len(cur)
            for i in range(curLen):
                if cur[i] != '(' and cur[i] !=')':
                    continue
                q.appendleft(cur[:i]+cur[i+1:])
        return ans


"""
this question is very similar to word ladder, but we don't need to keep track of the whole path

1. use deque to store visited words
2. use visited to avoid repeats
3. to create new words, remove every "(" and ")" from current word
4. when pop a word from queue, check if it's an answer, if answer is found, stop any deleting and only pop & check_valid all elements from the queue
5. to make sure we only save "minimum delete", FIFO, this way once an answer is found, everything left had equal num of deletes
"""