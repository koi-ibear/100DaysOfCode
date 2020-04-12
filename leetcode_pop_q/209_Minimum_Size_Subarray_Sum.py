"""
🌸 Medium 209. Minimum Size Subarray Sum
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 
"""

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        min_len = float('Inf')
        sums = 0
        left = 0
        for i in range(len(nums)):
            sums+=nums[i]
            while sums >= s:
                min_len = min(min_len, i+1-left)
                sums-=nums[left]
                left+=1
        if min_len < float('Inf'):
            return min_len
        return 0

"""
💬 
template:https://leetcode.com/problems/minimum-window-substring/discuss/26808/Here-is-a-10-line-template-that-can-solve-most-'substring'-problems
"""