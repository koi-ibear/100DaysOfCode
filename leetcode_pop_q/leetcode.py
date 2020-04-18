### Add Two Numbers
"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, ret=0) -> ListNode:
        result = step = ListNode(None)
        while l1 or l2 or ret:
            v1 = v2 = 0  ### saves time compared to checking l1.val + checking l1.next
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            ret, mod = divmod(v1+v2+ret, 10)
            step.next = ListNode(mod) ### important! move pointer to next
            step = step.next
        return result.next





### Find Minimum in Rotated Sorted Array Medium
"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
"""

class Solution:
    def findMinLoop(self, nums: List[int]) -> int:
        """
        while loop
        """
        b = len(nums) - 1
        a = 0
        if nums[a] < nums[b]:
            return nums[a]
        while b > a + 1:
            m = int((b+a)/2)
            if nums[m] > nums[a]:
                a = m
            else:
                b = m
        if nums[a] > nums[b]:
            return nums[b]
        else:
            return nums[a]
                           


    def findMinReccursion(self, nums: List[int]) -> int:
        """
        using reccursion
        """
        n = len(nums)
        m = int(n/2)
        o = 0
        if n > 2:
            if nums[o] > nums[m-1]:
                self.findMin(nums[o: m])
            elif nums[o] <= nums[m-1]:
                self.findMin(nums[m: n])
        return min(nums)





### Ransom Note
"""
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_sum = {}
        for i in magazine:
            try:
                mag_sum[i] += 1
            except KeyError:
                mag_sum[i] = 1
        for j in ransomNote:
            if j in mag_sum and mag_sum[j] > 0:
                mag_sum[j] = mag_sum[j] - 1
            else:
                return False
        return True
            
            
