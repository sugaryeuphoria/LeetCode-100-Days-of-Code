/*
1481. Least Number of Unique Integers after K Removals 
 * Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.
 * Example 1:

Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.
Example 2:
Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.
Constraints:

1 <= arr.length <= 10^5
1 <= arr[i] <= 10^9
0 <= k <= arr.length
*/
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Queue;
// Class definition
class Solution {
    // Method definition
    public int findLeastNumOfUniqueInts(int[] arr, int k) {
        // Step 1: Create a frequency map
        Map<Integer, Integer> count = new HashMap<>();
        
        // Count the frequency of each element in the array
        for (final int a : arr)
        count.merge(a, 1, Integer::sum);

        // Step 2: Create a min-heap to store frequencies
        Queue<Integer> minHeap = new PriorityQueue<>(count.values());

         // Step 3: Greedily remove the k least frequent numbers to have the least number of unique integers
        while (k > 0)
        k -= minHeap.poll(); //Remove the least frequent number from the min-heap
        
         // Step 4: Return the number of unique integers left after removals
        return minHeap.size() + (k < 0 ? 1 : 0); // If k is negative, one more unique integer is removed partially
    }
}