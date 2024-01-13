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
        # Iterate until either list1 or list2 becomes empty
        while list1 and list2:
            # Compare values of the current nodes in list1 and list2
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
             # Move the current pointer to the next node
            current = current.next

        # Append the remaining nodes from the non-empty list
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        # Return the head of the merged list
        return merged_head.next   
       
            