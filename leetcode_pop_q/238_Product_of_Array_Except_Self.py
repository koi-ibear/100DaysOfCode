"""
🌸 Medium 238. Product of Array Except Self
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]
        for i,j in enumerate(nums):
            ans.append(ans[i]*nums[i])
        ans.pop()
        r = 1
        for i in range(len(nums)-1, 0, -1):
            r = r*nums[i]
            ans[i-1] = ans[i-1]*r
        return ans

"""
💬
1. except -> binary split left vs. right
2. problem about division: 0s
"""