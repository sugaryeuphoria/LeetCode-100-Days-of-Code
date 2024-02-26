/*Reverse Integer 
 * Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 * 
*/
public class Day58 {
    
    // Method declaration
    public int reverse(int x) {
// Initialize a long variable to store the reversed number
        long ans = 0;
// Iterate until the input number becomes 0
        while (x != 0) {

// Multiply the current reversed number by 10 and add the last digit of the input number
            ans = ans * 10 + x % 10; 
// Remove the last digit from the input number
            x /= 10; 
        }
         // Check if the reversed number is within the range of 32-bit signed integer
    
        // If it's outside the range, return 0; otherwise, cast it to int and return
        return (ans < Integer.MIN_VALUE || ans > Integer.MAX_VALUE) ? 0 : (int) ans;

     }
}
