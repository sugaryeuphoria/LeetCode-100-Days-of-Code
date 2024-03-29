/*
 1669. Merge In Between Linked Lists
You are given two linked lists: list1 and list2 of sizes n and m respectively.
Remove list1's nodes from the ath node to the bth node, and put list2 in their place.
The blue edges and nodes in the following figure indicate the result:

Example 1:
Input: list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
Output: [10,1,13,1000000,1000001,1000002,5]
Explanation: We remove the nodes 3 and 4 and put the entire list2 in their place. The blue
edges and nodes in the above figure indicate the result.

Example 2:
Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]
Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]
Explanation: The blue edges and nodes in the above figure indicate the result.

Constraints:
3 <= list1.length <= 104
1 <= a <= b < list1.length - 1
1 <= list2.length <= 104
 */
class ListNode {
    int val;
    ListNode next;

    ListNode(int val) {
        this.val = val;
        this.next = null;
    }
}
class Day80 {
    public ListNode mergeInBetween(ListNode list1, int a, int b, ListNode list2) {
        // Traverse list1 to find the node before the ath node
        ListNode nodeBeforeA = list1;
        for (int i = 0; i < a - 1; ++i)
          nodeBeforeA = nodeBeforeA.next;
    
        // Find the bth node
        ListNode nodeB = nodeBeforeA.next;
        for (int i = 0; i < b - a; ++i)
          nodeB = nodeB.next;
    
        // Connect the node before A to the head of list2
        nodeBeforeA.next = list2;
        
        // Find the last node in list2
        ListNode lastNodeInList2 = list2;
        while (lastNodeInList2.next != null)
          lastNodeInList2 = lastNodeInList2.next;
    
        // Connect the last node in list2 to the node after B
        lastNodeInList2.next = nodeB.next;
        
        // Disconnect the nodes from A to B
        nodeB.next = null;
        
        // Return the modified list1
        return list1;
      }
    }


    