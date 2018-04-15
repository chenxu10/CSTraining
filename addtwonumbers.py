# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # corner cases
        # when one list is longer than the other
        # Initialize current code to dummy head of the returning list
        dummy=cur=ListNode(0)
        # Initialize carry to 0
        carry=0
        # Intialize p and q to head of l1 and l2 respectively
        # Loop through lists l1 and l2 until you reach both ends
        while l1 or l2 or carry:
            # set x to node p's value. if p has reached to the end of l1, set to 0
            if l1:
                carry+=l1.val
                l1=l1.next
            # set y to node q's value. if q has reached to the end of l2, set to 0
            if l2:
                carry+=l2.val
                l2=l2.next
            # set sum=x+y+carry
            # update carry=sum/10 and set it to current node's next, then advance current code to next
            cur.next=ListNode(carry%10)
            cur=cur.next
            carry//=10
            # advance both p and q
        # check if carry=1, if so append a new node with digit 1 to the returning list
        # return dummy head's next node
        return dummy.next
        # when one list is null
        # The sum need to carry