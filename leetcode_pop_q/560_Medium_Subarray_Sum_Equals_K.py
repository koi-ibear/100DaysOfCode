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
        csum = 0
        sum_tracker = {0:1}
        ans = 0
        for i in nums:
            csum += i # update running total
            ans += sum_tracker.get(csum - k, 0)
            sum_tracker[csum] = sum_tracker.get(csum,0)+1    
        return ans

"""
Hash + runnint total
as we move forward, keep track of running total,
find if new answer found by tracker.get(running_tot - k)
update tracker with current running total

we need to initialize dict with {0:1} because when running_tot == k, we want it to return 1
"""