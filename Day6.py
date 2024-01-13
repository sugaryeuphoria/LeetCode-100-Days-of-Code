# Definition for singly-linked list.
class ListNode(object):
    #method definition
    def createNode(self, val=0, next=None):
        # Constructor to create a new node with a given value and next node
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # Check if either list is empty
        if not list1:
            return list2
        if not list2:
            return list1
        
        # Initialize a dummy node to start the merged list
        merged_head = ListNode()
        current = merged_head

       