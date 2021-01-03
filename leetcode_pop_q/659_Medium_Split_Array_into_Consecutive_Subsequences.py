"""
🌸 Medium 659. Split Array into Consecutive Subsequences
Given an array nums sorted in ascending order, return true if and only if you can split it into 1 or more subsequences such that each subsequence consists of consecutive integers and has length at least 3.

Example 1:
Input: [1,2,3,3,4,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3
3, 4, 5

Example 2:
Input: [1,2,3,3,4,4,5,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3, 4, 5
3, 4, 5

Example 3:
Input: [1,2,3,4,4,5]
Output: False
"""
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        import collections
        cnt = collections.Counter(nums)
        tail = collections.Counter()
        for x in nums:
            # for unique numbers that are already included to a subseq, skip
            if cnt[x] == 0:
                continue
            # if some seq ends at x-1,  we COULD append x to this seq
            elif tail[x] > 0:
                tail[x] -= 1
                tail[x+1] += 1
            # if we can't extend existing seq, we COULD create a new seq if following 2 numbers exist
            elif cnt[x+1] > 0 and cnt[x+2] > 0:
                cnt[x+1] -= 1
                cnt[x+2] -= 1
                tail[x+3] += 1
            else:
                return False
            cnt[x] -= 1
        return True