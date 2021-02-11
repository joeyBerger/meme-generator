from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel
import pandas


class CSVImporter(IngestorInterface):
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path):
        """ Parses text from file, returns quote models """

        if not cls.can_ingest(path):
            raise Exception(f'Problem ingesting .csv file.'
                            f'Please check for correct format/corrupt file.')

        try:
            df = pandas.read_csv(path, header=0)
            quote_models = []

            for _, row in df.iterrows():
                quote_models.append(QuoteModel(row['body'], row['author']))

            return quote_models

        except BaseException:
            raise Exception('Error in ingesting .csv filetype')
