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

    def _find(self, u: int) -> int:
    # Find the root of the set containing element 'u' (with path compression).
        if self.id[u] != u:
            self.id[u] = self._find(self.id[u])  # Path compression
        return self.id[u]  # Return the root
    
    class Solution:
     def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
    # Initialize UnionFind object
        uf = UnionFind(n)

        # Dictionary to store meetings grouped by time
    timeToPairs = collections.defaultdict(list)

    # Start the first meeting with 'firstPerson'
    uf.unionByRank(0, firstPerson)

     # Group meetings by time
    for x, y, time in meetings:
      timeToPairs[time].append((x, y))

      # Process meetings in chronological order
    for _, pairs in sorted(timeToPairs.items(), key=lambda x: x[0]):
      peopleUnioned = set()

      # Union people attending the current meeting
      for x, y in pairs:
        uf.unionByRank(x, y)
        peopleUnioned.add(x)
        peopleUnioned.add(y)

         # Reset individuals who are not connected to the first person after the meeting
      for person in peopleUnioned:
        if not uf.connected(person, 0):
          uf.reset(person)

           # Find all people connected to the first person
    return [i for i in range(n) if uf.connected(i, 0)]
    
