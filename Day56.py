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