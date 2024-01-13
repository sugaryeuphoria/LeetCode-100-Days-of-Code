# Definition for singly-linked list.
class ListNode(object):
    #method definition
    def createNode(self, val=0, next=None):
        # Constructor to create a new node with a given value and next node
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
       