"""
Medium 18. 4Sum

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Notice that the solution set must not contain duplicate quadruplets.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [], target = 0
Output: []
 

Constraints:

0 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
Accepted
400,094
Submissions
1,142,799
"""
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        res = []
        for i in range(length):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            for j in range(length-1, -1, -1):
                if j <length-1 and nums[j] == nums[j+1]:
                    continue
                l = i+1
                r = j-1
                while l < r:
                    cur = [nums[i], nums[l], nums[r], nums[j]]
                    if sum(cur) == target:
                        res.append(cur)
                        while l < r and nums[l] == nums[l+1]:
                            l+=1
                        while l < r and nums[r] == nums[r-1]:
                            r-=1
                        l+=1
                        r-=1
                    elif sum(cur) < target:
                        l+=1
                    else:
                        r-=1
        return res
            