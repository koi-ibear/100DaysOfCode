"""
🌸 Medium 801. Minimum Swaps To Make Sequences Increasing

We have two integer sequences A and B of the same non-zero length.

We are allowed to swap elements A[i] and B[i].  Note that both elements are in the same index position in their respective sequences.

At the end of some number of swaps, A and B are both strictly increasing.  (A sequence is strictly increasing if and only if A[0] < A[1] < A[2] < ... < A[A.length - 1].)

Given A and B, return the minimum number of swaps to make both sequences strictly increasing.  It is guaranteed that the given input always makes it possible.

Example:
Input: A = [1,3,5,4], B = [1,2,3,7]
Output: 1
Explanation: 
Swap A[3] and B[3].  Then the sequences are:
A = [1, 3, 5, 7] and B = [1, 2, 3, 4]
which are both strictly increasing.
"""
class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        cur_swap = 1  # num of swaps needed to swap current element
        cur_fix = 0  # number of swaps needed to keep current element unchanged
        for i in range(1, len(A)):
            if A[i] <= A[i-1] or B[i] <= B[i-1]: # i'th operation is opposite to i-1
                temp = cur_swap
                cur_swap = cur_fix + 1 # moves needed to keep i-1 fix + swap current pair
                cur_fix = temp # moves needed to swap i-1 + 0 (keep current pair unchanged)
            elif A[i] <= B[i-1] or B[i] <= A[i-1]: # i'th operation is same as i-1
                cur_swap += 1
            else: # doesn't matter whether swap or not -- pick fewest moves
                min_ = min(cur_swap, cur_fix)
                cur_swap = min_ + 1
                cur_fix = min_
        return min(cur_fix, cur_swap)
