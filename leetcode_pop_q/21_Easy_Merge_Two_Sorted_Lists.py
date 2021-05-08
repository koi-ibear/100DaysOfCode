"""
Easy 21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

Example 1:


Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: l1 = [], l2 = []
Output: []
Example 3:

Input: l1 = [], l2 = [0]
Output: [0]
 
"""
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = new = ListNode(None, None)
        while l1 or l2:
            if not l1:
                new.next = l2
                l2 = l2.next
            elif not l2:
                new.next = l1
                l1 = l1.next
            elif l1.val < l2.val:
                new.next = l1
                l1 = l1.next
            else:
                new.next = l2
                l2 = l2.next
            new = new.next
        return head.next
                