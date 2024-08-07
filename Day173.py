"""
2181. Merge Nodes in Between Zeros
You are given the head of a linked list, which contains a series of integers separated by 0's. The beginning and end of the linked list will have Node.val == 0.

For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes. The modified list should not contain any 0's.

Return the head of the modified linked list.

Example 1:


Input: head = [0,3,1,0,4,5,2,0]
Output: [4,11]
Explanation: 
The above figure represents the given linked list. The modified list contains
- The sum of the nodes marked in green: 3 + 1 = 4.
- The sum of the nodes marked in red: 4 + 5 + 2 = 11.

Example 2:


Input: head = [0,1,0,3,0,2,2,0]
Output: [1,3,4]
Explanation: 
The above figure represents the given linked list. The modified list contains
- The sum of the nodes marked in green: 1 = 1.
- The sum of the nodes marked in red: 3 = 3.
- The sum of the nodes marked in yellow: 2 + 2 = 4.

Constraints:

The number of nodes in the list is in the range [3, 2 * 105].
0 <= Node.val <= 1000
There are no two consecutive nodes with Node.val == 0.
The beginning and end of the linked list have Node.val == 0.
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Initialize a pointer to traverse the list
        current = head.next  # Skip the initial zero
        dummy = ListNode(0)  # Dummy node to ease the new list creation
        tail = dummy  # Tail pointer for the new list
        sum_between_zeros = 0

        # Traverse the list
        while current:
            if current.val != 0:
                # Accumulate sum if current node is not zero
                sum_between_zeros += current.val
            else:
                # When a zero is encountered, it indicates the end of a segment
                if sum_between_zeros != 0:
                    # Create a new node with the accumulated sum
                    tail.next = ListNode(sum_between_zeros)
                    # Move the tail pointer to the new node
                    tail = tail.next
                    # Reset the accumulator
                    sum_between_zeros = 0
            # Move to the next node
            current = current.next

        # Return the next of dummy node which points to the head of the modified list
        return dummy.next

