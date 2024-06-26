
/*1382. Balance a Binary Search Tree 
Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.
A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

Example 1:
Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.

Example 2:
Input: root = [2,1,3]
Output: [2,1,3]
 
Constraints:

The number of nodes in the tree is in the range [1, 104].
1 <= Node.val <= 105
*/
import java.util.ArrayList;
import java.util.List;

// Definition for a binary tree node.
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {
    }

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class Day166 {
    public TreeNode balanceBST(TreeNode root) {
        // Step 1: Get sorted values via in-order traversal
        List<Integer> sortedValues = new ArrayList<>();
        inorderTraversal(root, sortedValues);
        // Step 2: Build balanced BST from sorted values
        return buildBalancedBST(sortedValues, 0, sortedValues.size() - 1);
    }

    private void inorderTraversal(TreeNode node, List<Integer> sortedValues) {
        // Base case: if the node is null, return
        if (node == null) {
            return;
        }
        // Recursively traverse the left subtree
        inorderTraversal(node.left, sortedValues);
        // Add the current node's value to the sorted values list
        sortedValues.add(node.val);
        // Recursively traverse the right subtree
        inorderTraversal(node.right, sortedValues);
    }

    private TreeNode buildBalancedBST(List<Integer> sortedValues, int start, int end) {
        // Base case: if start index is greater than end index, return null
        if (start > end) {
            return null;
        }
        // Find the middle index of the current sublist
        int mid = start + (end - start) / 2;
        // Create a new TreeNode with the middle element's value
        TreeNode node = new TreeNode(sortedValues.get(mid));
        // Recursively build the left subtree from the left sublist
        node.left = buildBalancedBST(sortedValues, start, mid - 1);
        // Recursively build the right subtree from the right sublist
        node.right = buildBalancedBST(sortedValues, mid + 1, end);
        // Return the current node
        return node;
    }
}
