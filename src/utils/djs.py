class DisjointSet:
    def __init__(self, num):
        self.parent = list(range(num))
        self.rank = [1] * num

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)

        if xroot == yroot:
            return False

        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = self.parent[yroot]
        elif self.rank[yroot] < self.rank[xroot]:
            self.parent[yroot] = xroot
        else:
            self.rank[xroot] = yroot
            self.rank[yroot] += 1

        return True
