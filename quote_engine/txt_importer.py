from .ingestor_interface import IngestorInterface
from .QuoteModel import QuoteModel

class TxtImporter(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path):
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        
        quote_models = []

        with open(path, 'r', encoding='utf-8-sig') as fp:
            contents = fp.read().split('\n')
            for entry in contents:
                parsed = entry.split(cls.delimiter)
                quote_models.append(QuoteModel(parsed[0],parsed[1]))

        return quote_models