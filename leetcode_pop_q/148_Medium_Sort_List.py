"""
Medium 148. Sort List

Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []
"""
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        """
        with recursion
        divide & conquer
        divide: use recursion to break list from the middle
        conquer: at the end of a divide, merge sort
        """
        if not head or not head.next: return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head1 = slow.next
        slow.next = None
        h0 = self.sortList(head)
        h1 = self.sortList(head1)
        return self.mergeSort(h0, h1)
        
    def mergeSort(self, head0, head1):
        ans = tmp = ListNode(0)
        while head0 and head1:
            if head0.val > head1.val:
                tmp.next = head1
                head1 = head1.next
            else:
                tmp.next = head0
                head0 = head0.next
            tmp = tmp.next
        tmp.next = head0 or head1
        return ans.next
        


class Solution:
    """
    without recursion (O(1) space)
    """
    def getSize(self, head):
        """
        find length of linked list. O(N)
        """
        res = 0
        while head:
            head = head.next
            res += 1
        return res
        
    def split(self, head, k):
        """
        split linked list with k elements from head
        return k+1 element (disconnected from prev)
        """
        if not head: return None
        i = 1
        while i < k and head:
            head = head.next
            i += 1
        if not head: return None
        res = head.next
        head.next = None
        return res
    
    def merge(self, l, r, head):
        """
        merge left right at the end of head
        return the last node after merge
        """
        tmp = head
        while l and r:
            if l.val < r.val:
                tmp.next = l
                l = l.next
            else:
                tmp.next = r
                r = r.next
            tmp = tmp.next
        tmp.next = l or r
        while tmp.next:
            tmp = tmp.next
        return tmp
    
    def sortList(self, head: ListNode) -> ListNode:
        size = self.getSize(head)
        step = 1
        dummy = ListNode(0)
        dummy.next = head
        while step < size:
            tmp = dummy
            cur = dummy.next
            while cur:
                l = cur
                r = self.split(l, step)
                cur = self.split(r, step)
                tmp = self.merge(l, r, tmp)
            step = step * 2
        return dummy.next

