"""
Medium 179. Largest Number

Given a list of non-negative integers nums, arrange them such that they form the largest number.

Note: The result may be very large, so you need to return a string instead of an integer.

Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"
Example 3:

Input: nums = [1]
Output: "1"
Example 4:

Input: nums = [10]
Output: "10"
"""
class Solution:
    def compare(self, s1, s2):
        """
        compare in which order should s1 and s2 go
        return true if s1s2 > s2s1
        """
        if s1+s2 > s2+s1:
            return True
        return False

    def merge(self, l, r):
        """
        merge two lists into one
        """
        new = []
        a, b = len(l), len(r)
        i, j = 0, 0
        while i < a and j < b:
            if self.compare(l[i], r[j]):
                new.append(l[i])
                i += 1
            else:
                new.append(r[j])
                j += 1
        new.extend(l[i:] or r[j:])
        return new
                 
    def mergeSort(self, nums, l, r):
        if l > r: return
        if l == r: return [nums[l]]
        m = (l+r)//2
        l = self.mergeSort(nums, l, m)
        r = self.mergeSort(nums, m+1, r)
        return self.merge(l, r)
        
    def largestNumber(self, nums: List[int]) -> str:
        """
        merge sort
        """
        nums = [str(i) for i in nums]
        return str(int("".join(self.mergeSort(nums, 0, len(nums)-1))))
        
        