"""
25. Reverse Nodes in k-Group
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a
 multiple of k then left-out nodes, in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000
 

Follow-up: Can you solve the problem in O(1) extra memory space?
"""
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
         # Function to reverse a group of k nodes starting from the head
        def reverse(head, k):
            prev = None
            curr = head
            for _ in range(k):
                if not curr:
                      return head, None  
                # If less than k nodes are remaining, return the head of the current group and None
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                return prev, head  # Return the head and tail of the reversed group
            count = 0
        curr = head
        while curr and count < k:
            curr = curr.next
            count += 1
        if count < k:
            return head  # 
        # Reverse the first group of k nodes
        new_head, new_tail = reverse(head, k)
        # Recursively reverse the remaining groups of k nodes
        new_tail.next = self.reverseKGroup(curr, k)
        return new_head
    
