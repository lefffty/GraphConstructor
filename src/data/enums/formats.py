from enum import StrEnum, auto


class ParseFormat(StrEnum):
    ADJAENCY_MATRIX = 'Adjaency matrix'
    ADJAENCY_LIST = 'Adjaency list'
    EDGES_LIST = 'Edges list'
    UNKNOWN = auto()
