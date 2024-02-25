/*2709. Greatest Common Divisor Traversal
 * You are given a 0-indexed integer array nums, and you are allowed to traverse between its indices. You can traverse between index i and index j, i != j, if and only if gcd(nums[i], nums[j]) > 1, where gcd is the greatest common divisor.

Your task is to determine if for every pair of indices i and j in nums, where i < j, there exists a sequence of traversals that can take us from i to j.

Return true if it is possible to traverse between all such pairs of indices, or false otherwise.
 * 
 */
import java.util.*;

class UnionFind {
  public UnionFind(int n) {
    // Initialize arrays for id and sz (size)
    id = new int[n];
    sz = new int[n];
    // Initialize each element's id to itself and size to 1
    for (int i = 0; i < n; ++i)
      id[i] = i;
    for (int i = 0; i < n; ++i)
      sz[i] = 1;
  }

  // Method to perform union by size
  public void unionBySize(int u, int v) {
    final int i = find(u);
    final int j = find(v);
    if (i == j)
      return;
    if (sz[i] < sz[j]) {
      // Update size and id arrays based on the sizes of components
      sz[j] += sz[i];
      id[i] = j;
    } else {
      sz[i] += sz[j];
      id[j] = i;
    }
  }

  // Method to get the size of the component containing element i
  public int getSize(int i) {
    return sz[i];
  }

  private int[] id; // Array to store parent of each element
  private int[] sz; // Array to store size of each component

  // Method to find the root of the component containing element u
  private int find(int u) {
    return id[u] == u ? u : (id[u] = find(id[u])); // Path compression
  }
}

class Solution {
  // Method to check if it's possible to traverse all pairs of indices
  public boolean canTraverseAllPairs(int[] nums) {
    final int n = nums.length;
    final int maxNum = Arrays.stream(nums).max().getAsInt();
    // Calculate minimum prime factors using Sieve of Eratosthenes
    final int[] minPrimeFactors = sieveEratosthenes(maxNum + 1);
    Map<Integer, Integer> primeToFirstIndex = new HashMap<>();
    UnionFind uf = new UnionFind(n);

    // Process each number and its prime factors
    for (int i = 0; i < n; ++i)
      for (final int primeFactor : getPrimeFactors(nums[i], minPrimeFactors))
        // Union indices based on shared prime factors
        if (primeToFirstIndex.containsKey(primeFactor))
          uf.unionBySize(primeToFirstIndex.get(primeFactor), i);
        else
          primeToFirstIndex.put(primeFactor, i);

    // Check if any component covers all indices
    for (int i = 0; i < n; ++i)
      if (uf.getSize(i) == n)
        return true;
    return false;
  }

  // Sieve of Eratosthenes algorithm to calculate minimum prime factors
  private int[] sieveEratosthenes(int n) {
    int[] minPrimeFactors = new int[n + 1];
    for (int i = 2; i <= n; ++i)
      minPrimeFactors[i] = i;
    for (int i = 2; i * i < n; ++i)
      if (minPrimeFactors[i] == i) // `i` is prime.
        for (int j = i * i; j < n; j += i)
          minPrimeFactors[j] = Math.min(minPrimeFactors[j], i);
    return minPrimeFactors;
  }

  // Method to get prime factors of a number
  private List<Integer> getPrimeFactors(int num, int[] minPrimeFactors) {
    List<Integer> primeFactors = new ArrayList<>();
    while (num > 1) {
      final int divisor = minPrimeFactors[num];
      primeFactors.add(divisor);
      while (num % divisor == 0)
        num /= divisor;
    }
    return primeFactors;
  }
}
