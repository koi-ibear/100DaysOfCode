"""
Medium 55. Jump Game

Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

 
Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        for i,j in enumerate(nums):
            if reach < i:
                return False
            reach = max(reach, i+j)
        return True
        
    # def canJump(self, nums: List[int]) -> bool:
    #     """
    #     X time limit exceeded
    #     """
    #     n = len(nums)
    #     visited = set()
    #     dp = [0] * n
    #     dp[0] = 1
    #     for i in range(n):
    #         if dp[i] == 0: continue
    #         for j in range(1, nums[i]+1):
    #             if i+j in visited:
    #                 continue
    #             elif i+j < n:
    #                 dp[i+j] += 1
    #                 visited.add(i+j)
    #     # print(dp)
    #     return dp[-1] > 0