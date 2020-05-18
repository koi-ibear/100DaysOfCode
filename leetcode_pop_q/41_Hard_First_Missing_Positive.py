"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        n = len(nums)
        ## first loop: get rid of numbers out of range
        for i in range(n):
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0
        ## second loop: track appearance of each number with index in the array
        for i in range(n):
            nums[nums[i]%n] += n
        ## third loop: any index > 0 that has value < n means they haven't been updated, return the first one
        for i in range(1, n):
            if nums[i]//n == 0:
                return i
        return n

"""
💬
We use array elements as index. To mark presence of an element x, we change the value at the index x to negative
https://www.geeksforgeeks.org/find-the-smallest-positive-number-missing-from-an-unsorted-array/
"""