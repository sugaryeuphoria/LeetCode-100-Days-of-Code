// Class definition

import java.util.ArrayList;
import java.util.List;

public class Day55 {
    // Method definition
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
        }
    }  

