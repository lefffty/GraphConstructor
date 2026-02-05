from enum import StrEnum, auto


class ParseFormat(StrEnum):
    ADJAENCY_MATRIX = 'Adjaency matrix'
    ADJAENCY_ARRAY = 'Adjaency array'
    ADJAENCY_LIST = 'Adjaency list'
    UNKNOWN = auto()
