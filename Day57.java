/*2709. Greatest Common Divisor Traversal
 * You are given a 0-indexed integer array nums, and you are allowed to traverse between its indices. You can traverse between index i and index j, i != j, if and only if gcd(nums[i], nums[j]) > 1, where gcd is the greatest common divisor.

Your task is to determine if for every pair of indices i and j in nums, where i < j, there exists a sequence of traversals that can take us from i to j.

Return true if it is possible to traverse between all such pairs of indices, or false otherwise.
 * 
 */
// Class and method declaration
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
}// Method to perform union by size
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
    }}