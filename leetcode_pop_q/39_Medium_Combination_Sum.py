"""
Medium 39. Combination Sum

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
"""
class Solution:
    # def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    #     """
    #     basic version
    #     """
    #     ans = []
    #     def calcSum(chosen):
    #         cur_sum = sum(chosen)
    #         if cur_sum > target: # validility check
    #             return False
    #         if cur_sum == target: # stop rule
    #             chosen = sorted(chosen)
    #             if chosen not in ans:
    #                 ans.append(chosen)
    #         for c in candidates:
    #             calcSum(chosen+[c])
    #     calcSum([])
    #     return ans
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Optimized:
            pass target, path and candidate in dfs
            subtract candidate[i] from target
            pass sum[i:] to next iter
        """
        ans = []
        def calcSum(chosen, nums, target):
            if target < 0:
                return False
            if target == 0:
                ans.append(chosen)
                return
            for i in range(len(nums)):
                calcSum(chosen+[nums[i]], nums[i:], target-nums[i])
        calcSum([], candidates, target)
        return ans