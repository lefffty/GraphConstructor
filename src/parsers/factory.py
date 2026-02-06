from pathlib import Path

from src.data.enums.formats import ParseFormat

from .edges_list import EdgesListParser
from .adjaency_list import AdjaencyListParser
from .adjaency_matrix import AdjaencyMatrixParser


class GraphParserFactory:
    @staticmethod
    def createParserToGraph(parseFormat: ParseFormat, filepath: Path):
        format_to_parser = {
            ParseFormat.ADJAENCY_MATRIX: AdjaencyMatrixParser,
            ParseFormat.ADJAENCY_LIST: AdjaencyListParser,
            ParseFormat.EDGES_LIST: EdgesListParser,
        }

        try:
            parser = format_to_parser[parseFormat](filepath)
        except KeyError:
            print('Invalid parsing format!')

        return parser
