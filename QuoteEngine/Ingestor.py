from DocxImporter import DocxImporter
from TxtImporter import TxtImporter
from CSVImporter import CSVImporter
from PDFImporter import PDFImporter

class Ingestor():
    ingestors = [DocxImporter,TxtImporter,CSVImporter,PDFImporter]
        
    @classmethod
    def parse(cls, path):
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)