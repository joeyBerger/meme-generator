from .docx_ingestor import DocxImporter
from .txt_ingestor import TxtImporter
from .csv_ingestor import CSVImporter
from .pdf_ingestor import PDFImporter


class Ingestor():
    ingestors = [DocxImporter, TxtImporter, CSVImporter, PDFImporter]

    @classmethod
    def parse(cls, path):
        """ Tries parsing file with given path"""

        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
