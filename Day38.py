"""You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself."""
# Method and class definition
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        dummy = ListNode(0)
        curr = dummy
    
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0