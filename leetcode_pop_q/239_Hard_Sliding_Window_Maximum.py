"""
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Follow up:
Could you solve it in linear time?

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 """
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or len(nums) == 0:
            return
        q = deque()
        for i in range(k):
            while len(q) > 0 and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
        res = []
        for i in range(k, len(nums)):
            res.append(nums[q[0]])
            if q[0] < i-k+1:
                q.popleft()
            while len(q) > 0 and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
        res.append(nums[q[0]])
        return res


"""
💬
1. monotonic Q
assuming there's a line and you can cut if you beat the person in front

2. index wise:
alwasy one step after the right end of the window
"""        