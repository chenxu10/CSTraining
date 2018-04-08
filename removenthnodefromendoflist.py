# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # dummy ->1->2->3->4->5
        #               s
        #                     f
        # create a dummy node
        dummy=ListNode(0)
        dummy.next=head
        slow=fast=dummy=0

        for _ in range(n):
        # fast先走两次
            fast=fast.next

        while fast.next:
            slow=slow.next
            fast=fast.next

        slow.next=slow.next.next

        return  dummy.next


