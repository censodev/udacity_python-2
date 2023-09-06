from modules.QuoteEngine.ingestor_interface import IngestorInterface
from modules.QuoteEngine.quote_model import QuoteModel


class TextIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path: str) -> list[QuoteModel]:
        rs = []
        with open(path) as fi:
            lines = fi.readlines()
            for line in lines:
                parts = line.split(' - ')
                rs.append(QuoteModel(parts[0], parts[1]))
        return rs
