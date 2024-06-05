/* 1002. Find Common Characters
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]
 
Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.
*/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Day145 {
    public List<String> commonChars(String[] A) {
         // Initialize the result list to store common characters
        List<String> ans = new ArrayList<>();
        // Initialize an array to keep track of the minimum frequency of each character
        int[] commonCount = new int[26];
        // Fill the array with the maximum integer value
        Arrays.fill(commonCount, Integer.MAX_VALUE);
        // Loop through each string in the input array
        for (String a : A) {
            // Initialize an array to count the frequency of each character in the current string
            int[] count = new int[26];
            // Loop through each character in the current string
            for (char c : a.toCharArray())
                // Increment the count for the character
                ++count[c - 'a'];
            // Update the commonCount array to hold the minimum frequency of each character seen so far
            for (int i = 0; i < 26; ++i)
            commonCount[i] = Math.min(commonCount[i], count[i]);
  }
        }
    }
}
