import os
import subprocess
from modules.QuoteEngine.ingestor_interface import IngestorInterface
from modules.QuoteEngine.quote_model import QuoteModel
from modules.QuoteEngine.text_ingestor import TextIngestor


class PDFIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path: str) -> list[QuoteModel]:
        tmp_file = './tmp_pdf_to_text.txt'
        cmd = f"./pdftotext.exe -nopgbrk -layout {path} {tmp_file}"
        subprocess.call(cmd, stderr=subprocess.STDOUT)
        rs = TextIngestor.parse(tmp_file)
        os.remove(tmp_file)
        return rs
