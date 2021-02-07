import pandas

from IngestorInterface import IngestorInterface
from QuoteModel import QuoteModel

class CSVImporter(IngestorInterface):
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path):
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        df = pandas.read_csv(path, header=0)
        quote_models = []

        for index, row in df.iterrows():
            quote_models.append(QuoteModel(row['body'],row['author']))

        return quote_models