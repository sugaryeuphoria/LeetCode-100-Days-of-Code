/*633. Sum of Square Numbers
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5

Example 2:

Input: c = 3
Output: false

Constraints:

0 <= c <= 231 - 1
*/
// Include cmath library for the sqrt function
#include <cmath>
class Solution {
 public:
  // Function to determine if there are two integers a and b such that a^2 + b^2 = c
  bool judgeSquareSum(int c) {
    // Initialize left pointer (l) to 0
    unsigned l = 0;

}