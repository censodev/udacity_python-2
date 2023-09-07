import os
import subprocess
from modules.QuoteEngine.ingestor_interface import IngestorInterface
from modules.QuoteEngine.quote_model import QuoteModel
from modules.QuoteEngine.text_ingestor import TextIngestor
from utils import build_abs_local_path


class PDFIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path: str) -> list[QuoteModel]:
        tmp_file = build_abs_local_path('./tmp_pdf_to_text.txt')
        exe_file = build_abs_local_path('./pdftotext.exe')
        cmd = f"{exe_file} -nopgbrk -layout {path} {tmp_file}"
        subprocess.call(cmd, stderr=subprocess.STDOUT)
        rs = TextIngestor.parse(tmp_file)
        os.remove(tmp_file)
        return rs
