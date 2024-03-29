// Class definition

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Queue;

public class Day55 {
    // Method definition
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        // Create an array of lists to represent the graph
        List<Pair<Integer, Integer>>[] graph = new List[n];
        class Solution {
            public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
              // Create an array of lists to represent the graph
              List<Pair<Integer, Integer>>[] graph = new List[n];
          
              // Initialize each list in the array
              for (int i = 0; i < n; i++)
                graph[i] = new ArrayList<>();
          
              // Populate the graph with flight information
              for (int[] flight : flights) {
                final int u = flight[0]; // Departure city
                final int v = flight[1]; // Destination city
                final int w = flight[2]; // Price of the flight
                graph[u].add(new Pair<>(v, w)); // Add the flight to the adjacency list of the departure city
              }
          
              // Call Dijkstra's algorithm to find the shortest path
              return dijkstra(graph, src, dst, k);
            }
          
            // Dijkstra's algorithm implementation
            private int dijkstra(List<Pair<Integer, Integer>>[] graph, int src, int dst, int k) {
              // Initialize an array to store distances
              int[][] dist = new int[graph.length][k + 2];
              // Initialize all distances to infinity
              Arrays.stream(dist).forEach(A -> Arrays.fill(A, Integer.MAX_VALUE));
              // Initialize a priority queue to store vertices (d, u, stops)
              Queue<int[]> minHeap = new PriorityQueue<>((a, b) -> a[0] - b[0]);
          
              // Initialize distance from source to source with k+1 stops as 0
              dist[src][k + 1] = 0;
              // Add source vertex to the priority queue
              minHeap.offer(new int[] {dist[src][k + 1], src, k + 1});
          
              // Dijkstra's algorithm loop
              while (!minHeap.isEmpty()) {
                final int d = minHeap.peek()[0]; // Distance to the current vertex
                final int u = minHeap.peek()[1]; // Current vertex
                final int stops = minHeap.poll()[2]; // Number of stops left
          
                // If the current vertex is the destination, return the distance
                if (u == dst)
                  return d;
          
                // If no stops left, continue to the next iteration
                if (stops == 0)
                  continue;
          
                // Iterate over the adjacent vertices of the current vertex
                for (Pair<Integer, Integer> pair : graph[u]) {
                  final int v = pair.getKey(); // Adjacent vertex
                  final int w = pair.getValue(); // Weight of the edge from u to v
          
                  // If the new distance is smaller than the stored distance, update it
                  if (d + w < dist[v][stops - 1]) {
                    dist[v][stops - 1] = d + w;
                    // Add the new distance, vertex, and stops to the priority queue
                    minHeap.offer(new int[] {dist[v][stops - 1], v, stops - 1});
                  }
                }
              }
          
              // If no path found, return -1
              return -1;
            }
          }
          
        // Initialize each list in the array
        for (int i = 0; i < n; i++)
        graph[i] = new ArrayList<>();

        // Populate the graph with flight information
        for (int[] flight : flights) {
            final int u = flight[0]; // Departure city
      final int v = flight[1]; // Destination city
      final int w = flight[2]; // Price of the flight
      graph[u].add(new Pair<>(v, w)); // Add the flight to the adjacency list of the departure city

       // Call Dijkstra's algorithm to find the shortest path
    return dijkstra(graph, src, dst, k);
    }
    // Dijkstra's algorithm implementation
  private int dijkstra(List<Pair<Integer, Integer>>[] graph, int src, int dst, int k) {
    // Initialize an array to store distances
    int[][] dist = new int[graph.length][k + 2];
     // Initialize all distances to infinity
    Arrays.stream(dist).forEach(A -> Arrays.fill(A, Integer.MAX_VALUE));
     // Initialize a priority queue to store vertices (d, u, stops)
    Queue<int[]> minHeap = new PriorityQueue<>((a, b) -> a[0] - b[0]);
     // Initialize distance from source to source with k+1 stops as 0
    dist[src][k + 1] = 0;
     // Add source vertex to the priority queue
    minHeap.offer(new int[] {dist[src][k + 1], src, k + 1});
         // Dijkstra's algorithm loop
    while (!minHeap.isEmpty()) {
      final int d = minHeap.peek()[0]; // Distance to the current vertex
      final int u = minHeap.peek()[1]; // Current vertex
      final int stops = minHeap.poll()[2]; // Number of stops left
    }
     // If the current vertex is the destination, return the distance
     if (u == dst)
        return d;
     // If no stops left, continue to the next iteration
     if (stops == 0)
        continue;

        // Iterate over the adjacent vertices of the current vertex
      for (Pair<Integer, Integer> pair : graph[u]) {
        final int v = pair.getKey(); // Adjacent vertex
        final int w = pair.getValue(); // Weight of the edge from u to v

        // If the new distance is smaller than the stored distance, update it
        if (d + w < dist[v][stops - 1]) {
          dist[v][stops - 1] = d + w;
          // Add the new distance, vertex, and stops to the priority queue
          minHeap.offer(new int[] {dist[v][stops - 1], v, stops - 1});
        }
      }
    

    // If no path found, return -1
    return -1;
}  }

