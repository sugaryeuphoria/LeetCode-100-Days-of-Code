"""
141. Linked List Cycle
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.
Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.

"""
# Class and method definition
class Solution(object):
    def hasCycle(self, head):

        # Check if the linked list is empty or has only one node
        if not head or not head.next:
            return False
        
        # Initialize two pointers: slow and fast
        slow = head
        fast = head.next

         # Traverse the linked list until fast pointer reaches the end or meets slow pointer
        while slow != fast:

            # If fast pointer reaches the end, there is no cycle
            if not fast or not fast.next:
                return False
            
            # Move slow pointer one step forward
            slow = slow.next
            
