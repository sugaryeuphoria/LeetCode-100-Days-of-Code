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
    }
}