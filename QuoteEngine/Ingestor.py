from DocxImporter import DocxImporter
from TxtImporter import TxtImporter

class Ingestor():
    ingestors = [DocxImporter,TxtImporter]
        
    @classmethod
    def parse(cls, path):
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)