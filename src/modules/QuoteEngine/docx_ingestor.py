from modules.QuoteEngine.ingestor_interface import IngestorInterface
from modules.QuoteEngine.quote_model import QuoteModel
from docx import Document


class DocxIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path: str) -> list[QuoteModel]:
        doc = Document(path)
        rs = []
        for p in doc.paragraphs:
            if p.text:
                parts = p.text.split(' - ')
                rs.append(QuoteModel(parts[0], parts[1]))
        return rs
