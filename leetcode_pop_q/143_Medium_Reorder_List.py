"""
Medium 143. Reorder List

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.


Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
 

Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        solution 2: reverse second half
        """
        ## find middle
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        ## reverse second half
        parent = slow.next
        slow.next = None
        child = None
        while parent:
            tmp = parent.next
            parent.next = child
            child = parent
            parent = tmp
            
        ## relink
        cur1 = head
        cur2 = child
        while cur1 and cur2:
            tmp = cur1.next
            cur1.next = cur2
            cur1 = cur2
            cur2 = tmp
        return head

#     def reorderList(self, head: ListNode) -> None:
#         """
#         solution 1: with queue
#         Do not return anything, modify head in-place instead.
#         """
#         q = []
#         node = head.next
#         while node:
#             tmp = node.next
#             node.next = None
#             q.append(node)
#             node = tmp
        
#         cur = head
#         while q:
#             cur.next = q.pop()
#             cur = cur.next
#             if q:
#                 cur.next = q.pop(0)
#                 cur = cur.next
#         return head