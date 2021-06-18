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

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        al = 1
        zeroes = 0
        for i in nums:
            if i == 0:
                zeroes += 1
            else:
                al = al * i
        if zeroes > 1: 
            nums = [0]* len(nums)
        elif zeroes == 1:
            for i, j in enumerate(nums):
                if j == 0: 
                    nums[i] = al
                else:
                    nums[i] = 0
        else:
            for i, j in enumerate(nums):
                nums[i] = int(al/j)
        return nums

"""
💬
1. except -> binary split left vs. right
2. problem about division: 0s
"""