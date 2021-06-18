"""
Easy 53. Maximum Subarray

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        inplace dp
        """
        for i in range(1, len(nums)):
            nums[i] += max([0, nums[i-1]])
        return max(nums)

#     def maxSubArray(self, nums: List[int]) -> int:
#         """
#         dp
#         """
#         n = len(nums)
#         dp = [-float('inf')] * (n+1)
#         for i in range(1, n+1):
#             dp[i] = max([dp[i-1], 0]) +nums[i-1]
#         print(dp)
#         return max(dp)
    
    # def maxSubArray(self, nums: List[int]) -> int:
    #     """
    #     brute force -- time out
    #     """
    #     n = len(nums)
    #     ans = -float('inf')
    #     for i in range(n):
    #         for j in range(i+1, n+1):
    #             tmp = sum(nums[i:j])
    #             if tmp > ans:
    #                 ans = tmp
    #     return ans