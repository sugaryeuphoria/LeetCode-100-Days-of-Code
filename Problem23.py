"""
23. Merge k Sorted Lists
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 
Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
"""
import heapq

class Solution(object):
    def mergeKLists(self, lists):
         # Define a dummy head for the result linked list
        dummy = ListNode()
        current = dummy

         # Initialize a min-heap
        heap = []

         # Push the head of each linked list into the min-heap
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, node))

        # Merge the linked lists
        while heap:
            # Pop the minimum node from the min-heap
            val, node = heapq.heappop(heap)

             # Append the minimum node to the result linked list
            current.next = node
            current = current.next

             # If the popped node has a next node, push it into the min-heap
            if node.next:
                heapq.heappush(heap, (node.next.val, node.next))