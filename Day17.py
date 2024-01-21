# Definition for singly-linked list.
# class ListNode(object):
class Solution(object):
    #Method definition
     def deleteDuplicates(self, head):
        # Check if the linked list is empty or has only one node
        if not head or not head.next:
            return head
         # Start from the head of the linked list
        current = head
        # Traverse the linked list
        while current and current.next:
            # Check if the current node's value is equal to the next node's value
            if current.val == current.next.val:
                  # Skip the next node by updating the pointers
                current.next = current.next.next
            else:
                # Move to the next node
                current = current.next
            # The linked list with duplicates removed is the modified head
            return head