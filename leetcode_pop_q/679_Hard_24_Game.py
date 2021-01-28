"""
Hard 679. 24 Game
You have 4 cards each containing a number from 1 to 9. You need to judge whether they could operated through *, /, +, -, (, ) to get the value of 24.

Example 1:
Input: [4, 1, 8, 7]
Output: True
Explanation: (8-4) * (7-1) = 24
Example 2:
Input: [1, 2, 1, 2]
Output: False
Note:
The division operator / represents real division, not integer division. For example, 4 / (1 - 2/3) = 12.
Every operation done is between two numbers. In particular, we cannot use - as a unary operator. For example, with [1, 1, 1, 1] as input, the expression -1 - 1 - 1 - 1 is not allowed.
You cannot concatenate numbers together. For example, if the input is [1, 2, 1, 2], we cannot write this as 12 + 12.
"""
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        eps = 0.01
        def dfs(nums):
            # print(nums)
            cur_len = len(nums)
            if cur_len == 1:
                if abs(nums[0] - 24)  < eps:
                    return True
                return False
            
            for i in range(cur_len):
                for j in range(i+1, cur_len):
                    a = nums[i]
                    b = nums[j]
                    cur_list = [a+b, a-b, b-a, a*b]
                    if a > eps:
                        cur_list.append(b/a)
                    if b > eps:
                        cur_list.append(a/b)
                    keep = []
                    for k in range(cur_len):
                        if i == k or j == k:
                            continue
                        keep.append(nums[k])
                    for c in cur_list:
                        if dfs(keep+[c]): 
                            return True
            return False
        return dfs(nums)
"""
stop rule:
use input (nums) to track computed results, when there's one value & it's near 24, success

recursion part:
take two cards, calculate all possible combinations
for each possible combo, create new list with it and remaining candidates, enter another dfs
"""