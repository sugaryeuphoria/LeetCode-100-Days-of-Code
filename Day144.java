/*409. Longest Palindrome
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome.

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.

Constraints:

1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.
 
 */
class Solution {
    public int longestPalindrome(String s) {
        // Initialize the variable to store the length of the longest palindrome
        int ans = 0;
        // Create an array to count the frequency of each character (assuming ASCII)
        int[] count = new int[128];
        // Loop through each character in the string
        for (final char c : s.toCharArray())
            // Increment the frequency count for the character
            ++count[c];
        // Loop through the frequency counts of all characters
        for (final int freq : count)
            // If the frequency is even, add it to the answer, otherwise add the largest even number less than the frequency
            ans += freq % 2 == 0 ? freq : freq - 1;
        // Check if there is at least one character with an odd frequency
        final boolean hasOddCount = Arrays.stream(count).anyMatch(freq -> freq % 2 == 1);
        // If there is an odd frequency, add 1 to the result (for the center characterin the palindrome)
        return ans + (hasOddCount ? 1 : 0);

    }
}