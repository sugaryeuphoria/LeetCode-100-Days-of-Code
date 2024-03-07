"""
876. Middle of the Linked List
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

Constraints:
The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
"""
# Method and class definition
class Solution(object):
    def middleNode(self, head):
        # Initialize two pointers: slow and fast
        slow = head
        fast = head

        # Traverse the linked list until fast pointer reaches the end or the second to the end
        while fast and fast.next:
            # Move slow pointer one step forward
            slow = slow.next

            # Move fast pointer two steps forward
            fast = fast.next.next

             # At this point, slow pointer is at the middle node
                return slow
            
