"""
19.Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

 Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # Create a dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        first = dummy  # Initialize the first pointer to the dummy node
        second = dummy  # Initialize the second pointer to the dummy node
        
        # Move the second pointer n+1 steps ahead
        for i in range(n + 1):
            second = second.next
            
        # Move both pointers simultaneously until second reaches the end
        while second is not None:
            first = first.next
            second = second.next
        
        # Remove the nth node from the end
        first.next = first.next.next
        
        return dummy.next  # Return the updated head of the linked list
