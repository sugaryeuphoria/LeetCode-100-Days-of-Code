"""
1171. Remove Zero Sum Consecutive Nodes from Linked List

Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum
to 0 until there are no such sequences.
After doing so, return the head of the final linked list.  You may return any such answer.
(Note that in the examples below, all sequences are serializations of ListNode objects.)

Example 1:
Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.

Example 2:
Input: head = [1,2,3,-3,4]
Output: [1,2,4]

Example 3:
Input: head = [1,2,3,-3,-2]
Output: [1]

Constraints:
The given linked list will contain between 1 and 1000 nodes.
Each node in the linked list has -1000 <= node.val <= 1000.
"""
class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Create a dummy node to handle cases where the head is part of the zero-sum sequence
        dummy = ListNode(0)
        dummy.next = head
        prefix_sum = 0
        prefix_sum_map = {}
        prefix_sum_map[0] = dummy  # Initialize the prefix sum map with a sum of 0
        while head:
            prefix_sum += head.val
            # If the prefix sum is found in the prefix_sum_map, it means we found a zero-sum sequence
            if prefix_sum in prefix_sum_map:
                # Remove all nodes between the two occurrences of the prefix sum
                prev = prefix_sum_map[prefix_sum]
                node = prev.next
                curr_sum = prefix_sum + node.val
                while curr_sum != prefix_sum:
                    del prefix_sum_map[curr_sum]
                    node = node.next
                    curr_sum += node.val
                prev.next = node.next
            else:
                # Add the current prefix sum to the map
                prefix_sum_map[prefix_sum] = head
            head = head.next
        return dummy.next

