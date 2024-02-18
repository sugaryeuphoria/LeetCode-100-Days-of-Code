import java.util.PriorityQueue;

class Day50 {
    // Method declaration
    public int furthestBuilding(int[] heights, int bricks, int ladders) {
     // Initialize a priority queue to store the differences in heights that require bricks
     PriorityQueue<Integer> pq = new PriorityQueue<>();
    // Iterate through the buildings
    for (int i = 0; i < heights.length - 1; i++) {
        int diff = heights[i + 1] - heights[i];
         // If the difference is positive, it means we need bricks to reach the next building
         if (diff > 0) {
            // Add the difference to the priority queue
            pq.offer(diff);
            // If the size of the priority queue exceeds the number of available ladders,
                // we need to use bricks instead of ladders
                if (pq.size() > ladders) {
                    bricks -= pq.poll(); // Use bricks for the smallest difference
          // If we don't have enough bricks, return the current index
          if (bricks < 0) {
            return i;
                }
    }
    }
}