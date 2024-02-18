/*2402. Meeting Rooms III
 * You are given an integer n. There are n rooms numbered from 0 to n - 1.

You are given a 2D integer array meetings where meetings[i] = [starti, endi] means that a meeting will be held during the half-closed time interval [starti, endi). All the values of starti are unique.

Meetings are allocated to rooms in the following manner:

Each meeting will take place in the unused room with the lowest number.
If there are no available rooms, the meeting will be delayed until a room becomes free. The delayed meeting should have the same duration as the original meeting.
When a room becomes unused, meetings that have an earlier original start time should be given the room.
Return the number of the room that held the most meetings. If there are multiple rooms, return the room with the lowest number.

A half-closed interval [a, b) is the interval between a and b including a and not including b.

 
 * 
 */
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
// If we reach here, it means we can reach the last building
return heights.length - 1;
}}