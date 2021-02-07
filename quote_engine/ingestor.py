from .docx_importer import DocxImporter
from .txt_importer import TxtImporter
from .cvs_importer import CSVImporter
from .pdf_importer import PDFImporter

class Ingestor():
    ingestors = [DocxImporter,TxtImporter,CSVImporter,PDFImporter]
        
    @classmethod
    def parse(cls, path):
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)