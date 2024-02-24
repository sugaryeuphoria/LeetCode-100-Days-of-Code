class UnionFind:
  def __init__(self, n: int):
      # Initialize the Union-Find data structure with 'n' elements.
    self.id = list(range(n))  # 'id' represents the parent of each element
    self.rank = [0] * n        # 'rank' represents the depth of each tree

    def unionByRank(self, u: int, v: int) -> None:
    # Perform union by rank operation between sets containing elements 'u' and 'v'.
        i = self._find(u)  # Find the root of 'u'
        j = self._find(v)  # Find the root of 'v'

        if i == j:
            return           # If 'u' and 'v' are already in the same set, no need to union them
        
        if self.rank[i] < self.rank[j]:
            self.id[i] = j   # 
        
        elif self.rank[i] > self.rank[j]:
            self.id[j] = i   # Attach the root of 'v' to the root of 'u' if rank of 'v' is less

        else:
            self.id[i] = j   # If ranks are equal, arbitrarily choose one as parent and increase rank
            self.rank[j] += 1
        
    def connected(self, u: int, v: int) -> bool:
    # Check if elements 'u' and 'v' belong to the same set.
        return self._find(self.id[u]) == self._find(self.id[v])
    
    def reset(self, u: int) -> None:
        # Reset the parent of element 'u' to itself.
        self.id[u] = u