"""
Hard 315. Count of Smaller Numbers After Self

You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

 

Example 1:

Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
 
"""
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        moveleft = [0]*len(nums) # track number of elements moved to the left of each digit during a merge sort
        
        def mergeSort(enum):
            """
            helper function that does merge sort
            enum: [(index, value)] pair list
            base case: if enum only has 1 element, return itself
            compare last digit in left vs. last digit in right:
                if right[-1] > left[-1]: pop right
                else: left[-1] will have len(right) moved to its left, hence moveleft[left[-1]] += len(right)
            """
            len_ = len(enum)
            mid = int(len_ / 2)
            if mid:
                left = enum[:mid]
                right = enum[mid:]
                left = mergeSort(left)
                right = mergeSort(right)
                for i in range(len_)[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]: # if nothing left on right, can't pop right in else; to pop left in if, must have left
                        moveleft[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    # elif left and right and left[-1][1] > right[-1][1]:
                    else:
                        enum[i] = right.pop()
            return enum
        enums = mergeSort(list(enumerate(nums)))
        return moveleft
        