"""
Medium 128. Longest Consecutive Sequence

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        nums.sort()
        cur_lenth, ans = 1, 1
        for i in range(1, n):
            if nums[i] == nums[i-1]:
                continue
            elif nums[i] == nums[i-1] + 1:
                cur_lenth += 1
                ans = max(cur_lenth, ans)
            else:
                cur_lenth = 1
        return ans
    

    def longestConsecutive(self, nums: List[int]) -> int:
        """dirty trick"""
        nums = set(nums)
        if len(nums) <= 1: return len(nums)
        ans = 1
        for i in nums:
            if i-1 not in nums:
                j = i+1
                while j in nums:
                    j += 1
                ans = max(ans, j-i)
        return ans