/*344. Reverse String 
 Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.
*/

public class Day142 {
    public void reverseString(char[] s) {
        // Initialize the left pointer to the start of the array
        int l = 0;
        // Initialize the right pointer to the end of the array
        int r = s.length - 1;
    
        // Loop until the two pointers meet in the middle
        while (l < r) {
          // Store the character at the left pointer in a temporary variable
          char temp = s[l];
          // Copy the character from the right pointer to the left pointer and increment the left pointer
          s[l++] = s[r];
          // Copy the character from the temporary variable to the right pointer and decrement the right pointer
          s[r--] = temp;
        }
      }
    }
    
    
    
    
    