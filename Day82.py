"""
234. Palindrome Linked List
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false

Constraints:
The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
"""
class Solution {
    public boolean isPalindrome(ListNode head) {
 // Check if the list is empty or contains only one node
        if (head == null || head.next == null) {
return true; // An empty list or a single node is considered a palindrome
        }
        // Step 1: Find the middle of the linked list
        ListNode slow = head; // Slow pointer
        ListNode fast = head; // Fast pointer

        // Move the fast pointer two steps at a time and slow pointer one step at a time
        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        // Step 2: Reverse the second half of the linked list
        ListNode secondHalfHead = reverseLinkedList(slow.next);
    // Step 3: Compare the first half with the reversed second half
        ListNode p1 = head; // Pointer for the first half
        ListNode p2 = secondHalfHead; // Pointer for the reversed second half
    // Traverse both halves and compare corresponding nodes
        while (p2 != null) {
            if (p1.val != p2.val) {
                return false; // If values are not equal, it's not a palindrome
            }
            p1 = p1.next;
            p2 = p2.next;

        }
        return true; // If all values match, it's a palindrome
    // Helper function to reverse a linked list
    private ListNode reverseLinkedList(ListNode head) {
        ListNode prev = null; // Pointer to the previous node
        ListNode current = head; // Pointer to the current node
    }
}