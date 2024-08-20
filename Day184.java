/*1140. Stone Game II
Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones. 
Alice and Bob take turns, with Alice starting first.  Initially, M = 1.
On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).
The game continues until all the stones have been taken.
Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.
Example 1:

Input: piles = [2,7,9,4,4]
Output: 10
Explanation:  If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 piles in total. If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 
Example 2:

Input: piles = [1,2,3,4,5,100]
Output: 104 

Constraints:

1 <= piles.length <= 100
1 <= piles[i] <= 104
*/
class Solution {
    public int stoneGameII(int[] piles) {
        final int n = piles.length;
        // Get the number of piles
        int[][] mem = new int[n][n];
        // Create a memoization table 'mem' to store results of subproblems.
        // mem[i][M] will store the maximum stones Alice can collect starting from index
        // 'i' with 'M'.
        int[] suffix = new int[n];
        // Create a 'suffix' array where suffix[i] represents the sum of piles from
        // index 'i' to the end of the array.
        Arrays.stream(mem).forEach(A -> Arrays.fill(A, -1));
        // Initialize the memoization table with -1 to indicate that the subproblem
        // hasn't been computed yet.
        suffix[n - 1] = piles[n - 1];
        // Initialize the last element of the suffix array with the value of the last
        // pile, since it's the only element left.
        for (int i = n - 2; i >= 0; --i)
            // Fill the suffix array from the second last pile to the first pile.
            suffix[i] = suffix[i + 1] + piles[i];
        // For each pile, calculate the sum of piles from that index to the end by
        // adding the current pile to the sum of the next pile.
        return stoneGameII(suffix, 0, 1, mem);
        // Call the helper function to compute the maximum number of stones Alice can
        // collect starting from the first pile with M = 1.
    }

    // Helper function to return the maximum number of stones Alice can get from
    // piles[i..n) with M.
    private int stoneGameII(int[] suffix, int i, int M, int[][] mem) {
        if (i + 2 * M >= suffix.length)
            // Base case: If Alice can take all remaining piles (i.e., `i + 2 * M >= n`),
            // she takes all the stones.
            return suffix[i];

        if (mem[i][M] != -1)
            // If the result for this subproblem is already computed, return it to avoid
            // redundant calculations.
            return mem[i][M];

        int opponent = suffix[i];
        // Initialize 'opponent' with the total stones Alice can collect starting from
        // index 'i'.

        for (int X = 1; X <= 2 * M; ++X)
            // Try all possible moves where Alice takes between 1 and 2 * M piles.
            opponent = Math.min(opponent, stoneGameII(suffix, i + X, Math.max(M, X), mem));
        // The opponent will minimize the stones Alice can get, so find the minimum
        // value by taking the best move for the opponent.

        return mem[i][M] = suffix[i] - opponent;
        // Store the result in the memoization table and return the maximum stones Alice
        // can collect.
    }
}