/*11. Container With Most Water
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
 */
class Day146 {
    public int maxArea(int[] height) {
        // Initialize the maximum area to 0
        int ans = 0;
        // Initialize the left pointer to the beginning of the array
        int l = 0;
         // Initialize the right pointer to the end of the array
         int r = height.length - 1;
         // Loop until the two pointers meet
    while (l < r) {
        // Find the shorter of the two lines
        final int minHeight = Math.min(height[l], height[r]);
         // Calculate the area and update the maximum area if the current one is larger
         ans = Math.max(ans, minHeight * (r - l));


    }

}