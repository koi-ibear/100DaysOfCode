"""
Medium 416. Partition Equal Subset Sum


Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_ = sum(nums)
        len_ = len(nums)
        def sumHalf(nums, ind, target, valid, len_):
            if target in valid:
                return valid[target]
            if target == 0:
                valid[target] = 1
            else:
                valid[target] = 0
                if target > 0:
                    for i in range(ind, len_):
                        if sumHalf(nums, i+1, target-nums[i], valid, len_):
                            valid[target] = 1
                            break
            return valid[target]

        if sum_ % 2 !=0:
            return 0
        return sumHalf(nums, 0, sum_/2, {}, len_)>0

