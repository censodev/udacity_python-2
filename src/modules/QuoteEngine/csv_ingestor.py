from modules.QuoteEngine.ingestor_interface import IngestorInterface
from modules.QuoteEngine.quote_model import QuoteModel
import pandas


class CSVIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path: str) -> list[QuoteModel]:
        csv = pandas.read_csv(path)
        rs = []
        for rc in csv.to_numpy():
            rs.append(QuoteModel(rc[0], rc[1]))
        return rs
