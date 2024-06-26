/*1051. Height Checker
 A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in non-decreasing order by height. Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.

You are given an integer array heights representing the current order that the students are standing in. Each heights[i] is the height of the ith student in line (0-indexed).

Return the number of indices where heights[i] != expected[i].

Example 1:

Input: heights = [1,1,4,2,1,3]
Output: 3
Explanation: 
heights:  [1,1,4,2,1,3]
expected: [1,1,1,2,3,4]
Indices 2, 4, and 5 do not match.

Example 2:

Input: heights = [5,1,2,3,4]
Output: 5
Explanation:
heights:  [5,1,2,3,4]
expected: [1,2,3,4,5]
All indices do not match.

Example 3:

Input: heights = [1,2,3,4,5]
Output: 0
Explanation:
heights:  [1,2,3,4,5]
expected: [1,2,3,4,5]
All indices match.

Constraints:

1 <= heights.length <= 100
1 <= heights[i] <= 100
 */
class Solution {
    public int heightChecker(int[] heights) {
        // Initialize a variable to keep track of the number of out-of-order heights
        int ans = 0;
        // Initialize a variable to keep track of the current height being checked
        int currentHeight = 1;
        // Create an array to count the frequency of each height (heights range from 1
        // to 100)
        int[] count = new int[101];
        // Count the occurrences of each height in the input array
        for (int height : heights)
            ++count[height];
        // Iterate over the input array to check each height
        for (int height : heights) {
            // Find the next non-zero height in the count array
            while (count[currentHeight] == 0)
                ++currentHeight;
            // If the current height in the input array does not match the currentHeight,
            // increment ans
            if (height != currentHeight)
                ++ans;
            // Decrement the count of the currentHeight as it has been used
            --count[currentHeight];
        }
        // Return the total number of heights that are out of order
        return ans;
    }
}