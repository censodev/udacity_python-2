import os
from modules.QuoteEngine.quote_model import QuoteModel


class IngestorInterface:
    @classmethod
    def can_ingest(cls, path: str) -> bool:
        _, ext = os.path.splitext(path)
        return ext in ['.csv', '.docx', '.pdf', '.txt']

    @classmethod
    def parse(cls, path: str) -> list[QuoteModel]:
        pass
