"""
Medium 75. Sort Colors

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
Example 3:

Input: nums = [0]
Output: [0]
Example 4:

Input: nums = [1]
Output: [1]
"""

"""
https://en.wikipedia.org/wiki/Dutch_national_flag_problem
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        ## pt0 points to current 0, left to which are all 0s; 
        ## pt2 points to cur 2, right to which are all 2s
        pt0 = 0
        pt2 = n-1
        ## i points to the end of middle, hence i moves with pt0 & pt2 + 1
        i = 0
        ## for each i in nums, swap to pt0 & move pt0 if nums[i] is 0; similar for 2s
        while i <= pt2:
            if nums[i] == 0:
                nums[i] = nums[pt0]
                nums[pt0] = 0
                pt0 +=1
                i += 1
            elif nums[i] == 2:
                nums[i] = nums[pt2]
                nums[pt2] = 2
                pt2 -= 1
                ## i = i-1+1
            else:
                i += 1
        return nums