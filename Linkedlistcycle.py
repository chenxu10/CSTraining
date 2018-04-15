class Node:
    # constructor to initialize a node
    def __init__(self,data):
        self.data=date
        self.next=None
class LinkedList:
    # function to initialize a head
    def __init__(self):
        self.head=None

    # function to insert a new node at the beginning
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node

    # function to print the linkedlist
    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data,end=" ")
            temp=temp.next

# Method 1: use hash table
class Solution(object):
    def hasCycle(self,head):
        s=set()
        temp=head
        while(temp):
            if temp in s:
                return True
            s.add(temp)
            temp=temp.next
        return False
# Time complexity: O(n). visited each of the n elements in the list at most once
# Adding a node to the hash table costs only O(1) time.

# Space complexity: O(n) The space depends on the number of elements added to the
# hash table

# Method 2: Two Pointers
def hasCycle(self,head):
    try:
        slow=head
        fast=head.next
        while slow is not fast:
            slow=slow.next
            fast=fast.next.next
        return True
    except:
        return False

# Time complexity: no cycle O(n) has a cycle O(k) overall it's O(n)
# space complexity: only use two nodes(slow and fast), so the space complexity if O(1)

