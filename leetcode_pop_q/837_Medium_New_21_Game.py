"""
Medium 837. New 21 Game

Alice plays the following game, loosely based on the card game "21".

Alice starts with 0 points, and draws numbers while she has less than K points.  During each draw, she gains an integer number of points randomly from the range [1, W], where W is an integer.  Each draw is independent and the outcomes have equal probabilities.

Alice stops drawing numbers when she gets K or more points.  What is the probability that she has N or less points?

Example 1:

Input: N = 10, K = 1, W = 10
Output: 1.00000
Explanation:  Alice gets a single card, then stops.
Example 2:

Input: N = 6, K = 1, W = 10
Output: 0.60000
Explanation:  Alice gets a single card, then stops.
In 6 out of W = 10 possibilities, she is at or below N = 6 points.
Example 3:

Input: N = 21, K = 17, W = 10
Output: 0.73278

"""
class Solution:

#     def new21Game(self, N: int, K: int, W: int) -> float:
#         """
#         N: calculate P(tot <= N)
#         K: stop drawing when gets K points
#         W: draw from the intervao [1, W]
#         """
#         pr_win = [0] * (K+W)
#         for i in range(K, K+W):
#             if i > N:
#                 pr_win[i] = 0
#             else:
#                 pr_win[i] = 1
            
#         for i in range(K-1, -1, -1):
#             pr_win[i] = 1/W*sum(pr_win[i+1:i+W+1])
#         return pr_win[0]
            
    def new21Game(self, N: int, K: int, W: int) -> float:
        """
        N: calculate P(tot <= N)
        K: stop drawing when gets K points
        W: draw from the intervao [1, W]
        """
        pr_win = [0] * (K+W)
        s = 0
        for i in range(K, K+W):
            if i > N:
                pr_win[i] = 0
            else:
                pr_win[i] = 1
            s += pr_win[i]
            
        for i in range(K-1, -1, -1):
            pr_win[i] = s/W
            s = s + pr_win[i] - pr_win[i+W]
        return pr_win[0]
"""
# dynamic programming
# fill box
once reach K, result is certain: > N lose <= N win
    for x in (K, k+W):
        if K+x > N: 0; else 1
for [0, K-1], prob(win) = 1/W * (prob(x+1)+...+prob(x+W))

"""