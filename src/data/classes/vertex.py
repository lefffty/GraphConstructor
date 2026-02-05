from dataclasses import dataclass


@dataclass
class Vertex:
    name: str

    def rename(self, name: str):
        if not isinstance(name, str):
            raise ValueError
        self.name = name

    def to_serializable(self):
        return {
            'name': self.name,
        }

    def __gt__(self, other):
        return False

    def __str__(self):
        return 'Vertex({})'.format(self.name)

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other) -> bool:
        return self.name == other.name
