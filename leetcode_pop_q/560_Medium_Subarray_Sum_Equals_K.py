"""
Medium 560. Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        def dfs(nums, k):
            if k == 0:
                return 1
            if k < 0:
                 return 0
            n = len(nums)
            ans = 0
            for i in range(n):
                for j in range(i+1, n):
                    if dfs(nums[j:], k-sum(nums[i:j])):
                        ans += 1
            return ans
        return dfs(nums,k)