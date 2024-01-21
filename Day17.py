# Definition for singly-linked list.
# class ListNode(object):
class Solution(object):
    #Method definition
     def deleteDuplicates(self, head):
           # Check if the linked list is empty or has only one node
        if not head or not head.next:
            return head