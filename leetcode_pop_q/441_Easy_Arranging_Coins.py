"""441. Arranging Coins

You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
"""
class Solution:
    def arrangeCoins(self, n: int) -> int:
        """
        binary search res where
        (1+res)*res/2 <= n, 1<= res <= n
        """
        if n < 1:
            return 0
        left, right = 1, n
        while left <= right:
            tmp = (left+right)//2
            cur = tmp * (tmp + 1)
            if cur == 2*n:
                return tmp
            elif cur > 2*n:
                right = tmp - 1
            else:
                left = tmp + 1
        return right
"""
also see 35
"""