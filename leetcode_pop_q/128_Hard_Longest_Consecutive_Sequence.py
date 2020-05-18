"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = sorted(nums)
        max_len = cur_len = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                cur_len += 1
            elif nums[i] == nums[i-1]:
                cur_len += 0
            else:
                max_len = max(max_len, cur_len)
                cur_len = 1
        return max(max_len, cur_len)