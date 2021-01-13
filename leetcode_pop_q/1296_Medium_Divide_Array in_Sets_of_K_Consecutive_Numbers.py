"""
Medium 1296. Divide Array in Sets of K Consecutive Numbers

Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into sets of k consecutive numbers
Return True if its possible otherwise return False.

"""
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        from collections import Counter
        cntr = Counter(nums)
        for i in sorted(cntr):
            cur = cntr[i]
            if cur > 0:
                for j in range(k):
                    cntr[i+j] -= cur
                    if cntr[i+j] < 0:
                        return False
        return True