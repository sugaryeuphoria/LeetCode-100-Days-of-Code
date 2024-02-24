class UnionFind:
  def __init__(self, n: int):
      # Initialize the Union-Find data structure with 'n' elements.
    self.id = list(range(n))  # 'id' represents the parent of each element
    self.rank = [0] * n        # 'rank' represents the depth of each tree