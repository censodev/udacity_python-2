import os
from modules.QuoteEngine.quote_model import QuoteModel
from abc import ABC, abstractmethod


class IngestorInterface(ABC):
    @classmethod
    def can_ingest(cls, path: str) -> bool:
        _, ext = os.path.splitext(path)
        return ext in ['.csv', '.docx', '.pdf', '.txt']

    @abstractmethod
    def parse(cls, path: str) -> list[QuoteModel]:
        pass
