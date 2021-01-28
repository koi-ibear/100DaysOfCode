"""
Medium 40. Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def findSum(nums, target, cur_cand):
            if target < 0:
                return False
            if target == 0:
                # if cur_cand not in ans:
                ans.append(cur_cand)
                return True
            for i in range(len(nums)):
                if i == 0 or i > 0 and nums[i] > nums[i-1]:
                    findSum(nums[i+1:], target - nums[i], cur_cand + [nums[i]])
        findSum(sorted(candidates), target, [])
        return ans
"""
the difference from CombSumI 
1. every number can only be use once
2. candidate is NOT distinct any more


to avoid duplicates in ans, we need to
1. sort candidate first
2. skip duplicate candidates in loop

e.g.
1, 1, 2, 3, 4
findSum(nums[0:],...) covers ALL cases in findSum(nums[1:],...)

"""