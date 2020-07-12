”“”
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
“”“

from Queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        q = PriorityQueue()
        head = pointer = ListNode(0)
        for i in lists:
            if i:
                q.put((i.val, i)) # q.put((priority_order, obj))
        while not q.empty():
            val, node = q.get() # gets the minimum priority_order (value) from PQ
            pointer.next = ListNode(val)
            pointer = pointer.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next
