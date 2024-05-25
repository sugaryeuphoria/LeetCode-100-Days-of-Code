/*
140. Word Break II
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.
Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]

Example 2:

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []

Constraints:

1 <= s.length <= 20
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 10
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
Input is generated in a way that the length of the answer doesn't exceed 105.
 */

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

class Day136 {
    // Function to find all possible sentences from string 's' using words from 'wordDict'
    public List<String> wordBreak(String s, List<String> wordDict) {
      // Convert wordDict to a set for O(1) lookups
      Set<String> wordSet = new HashSet<>(wordDict);
      // Create a memoization map to store results for substrings
      Map<String, List<String>> mem = new HashMap<>();
      // Call the helper function with the initial string 's'
      return wordBreak(s, wordSet, mem);
    }
  
    // Helper function for the recursive word break process
    private List<String> wordBreak(final String s, Set<String> wordSet,
                                   Map<String, List<String>> mem) {
      // If the result for the current string 's' is already computed, return it
      if (mem.containsKey(s))
        return mem.get(s);
  
      // Initialize a list to store possible sentences
      List<String> ans = new ArrayList<>();
  
      // Loop through all possible prefixes of 's'
      // 1 <= prefix.length() < s.length() ensures that prefix is not empty and not the whole string
      for (int i = 1; i < s.length(); ++i) {
        // Extract the prefix from the start to the current index 'i'
        final String prefix = s.substring(0, i);
        // Extract the suffix from the current index 'i' to the end
        final String suffix = s.substring(i);
        // If the prefix is a valid word, recursively process the suffix
        if (wordSet.contains(prefix))
          // Concatenate prefix with each valid sentence from the suffix and add to the result
          for (final String word : wordBreak(suffix, wordSet, mem))
            ans.add(prefix + " " + word);
      }
  
      // If the whole string 's' is a valid word, add it to the result
      if (wordSet.contains(s))
        ans.add(s);
  
      // Memoize the result for the current string 's'
      mem.put(s, ans);
      // Return the list of possible sentences for the current string 's'
      return ans;
    }
  }
  
