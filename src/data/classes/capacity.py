from dataclasses import dataclass

from .edge import Edge, SupportsFloat


@dataclass
class CapacityEdge(Edge):
    used: SupportsFloat = 0.0

    def adjast_used(self, amount: SupportsFloat):
        if self.used + amount < 0.0 or self.used + amount > self.weight:
            raise ValueError("Capacity error!")
        self.used += amount

    def capacity_left(self):
        return self.weight - self.used

    def flow_used(self):
        return self.used


if __name__ == '__main__':
    pass
