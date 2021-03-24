"""
🌸 Medium 15. 3Sum

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.


Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        length = len(nums)
        for i in range(length):
            if i >0 and nums[i]==nums[i-1]:
                continue
            l = i+1
            r = length-1
            while l < r:
                cur = [nums[i], nums[l], nums[r]]
                if sum(cur) == 0:
                    res.append(cur)
                    while l < r and nums[l] == nums[l+1]:
                        l+=1
                    while r >l and nums[r] == nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
                elif sum(cur)<0:
                    l+=1 
                else:
                    r-=1
                
        return res
                    