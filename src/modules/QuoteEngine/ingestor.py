import os
from modules.QuoteEngine.csv_ingestor import CSVIngestor
from modules.QuoteEngine.docx_ingestor import DocxIngestor
from modules.QuoteEngine.ingestor_interface import IngestorInterface
from modules.QuoteEngine.pdf_ingestor import PDFIngestor
from modules.QuoteEngine.text_ingestor import TextIngestor
from modules.QuoteEngine.quote_model import QuoteModel


class Ingestor(IngestorInterface):
    @classmethod
    def parse(cls, path: str) -> list[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception("File's extention is not supported.")
        _, ext = os.path.splitext(path)
        if ext == '.csv':
            return CSVIngestor.parse(path)
        elif ext == '.docx':
            return DocxIngestor.parse(path)
        elif ext == '.pdf':
            return PDFIngestor.parse(path)
        elif ext == '.txt':
            return TextIngestor.parse(path)
