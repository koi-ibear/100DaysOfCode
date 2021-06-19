"""
Medium 322. Coin Change


You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
Example 4:

Input: coins = [1], amount = 1
Output: 1
Example 5:

Input: coins = [1], amount = 2
Output: 2
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        dp for each value 0, 1,... amount
        base case: amount = 0: dp = 0
        dp[x] = min(dp[x], dp[x-coin]) <- at each value, it's either already found combo or x-coin whichever is smaller <- this is why init value for dp should be inf so it gets updated
        """
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for j in coins:
                if i-j >= 0:
                    dp[i] = min(dp[i-j]+1, dp[i])
        print(dp)
        if dp[-1] == float('inf'):
            return -1
        return dp[-1]
    