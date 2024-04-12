"""
42. Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""
class Solution(object):
    def trap(self, height):
        # Check if the height list is empty
        if not height:
            return 0
         # Initialize two pointers at the beginning and end of the height list
        left, right = 0, len(height) - 1
        # Initialize variables to store the maximum height encountered from the left and right directions
        left_max, right_max = 0, 0
         # Initialize variable to store the total water trapped
        water_trapped = 0
        # Iterate until the left pointer is less than the right pointer
        while left < right:
             # Check if the height at the left pointer is less than the height at the right pointer
            if height[left] < height[right]:
                # Update the left_max if the current height is greater than or equal to left_max
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                     # Add the difference between left_max and the current height to water_trapped
                    water_trapped += left_max - height[left]
                    # Move the left pointer to the right
                left += 1
            else: