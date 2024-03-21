/* 
206. Reverse Linked List
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
 
Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
*/
class Day81 {

        // Define a method to reverse a linked list
        public ListNode reverseList(ListNode head) {

          // Check if the head is null or if it's the last node in the list
          if (head == null || head.next == null)
            return head; // If so, return the head as it is (base case)
      
          // Recursively call reverseList to reverse the rest of the list
          ListNode newHead = reverseList(head.next);
          
          // Reverse the pointers to reverse the order of nodes
          // Make the next node's next pointer point back to the current node
          head.next.next = head; 
          
          // Set the current node's next pointer to null to avoid cycles
          head.next = null; 

          // Return the new head of the reversed list
          return newHead;
        }
      }
      