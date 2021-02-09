"""
Medium 279. Perfect Squares

Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

 

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
 
"""
class Solution:
    def numSquares(self, n: int) -> int:
        ## create elements of perfect numbers smaller than n
        elements = []
        for i in range(n, 0, -1):
            cur = i*i
            if cur <= n:
                elements.append(cur)
        q = collections.deque()
        q.appendleft((0, [], 0))
        found = 0
        while q:
            newq = collections.deque()
            for i in range(len(q)):
                cur, trace, counter = q.pop()
                for e in elements:
                    new = e+cur
                    if new == n:
                        return counter + 1
                    if new < n:          
                        newq.appendleft((new, trace+[e], counter+1))
            q = newq
        return