from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel


class TxtImporter(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path):
        """ Parses text from file, returns quote models """

        if not cls.can_ingest(path):
            raise Exception(f'Problem ingesting .txt file.'
                            f'Please check for correct format/corrupt file.')

        quote_models = []

        try:
            with open(path, 'r', encoding='utf-8-sig') as fp:
                contents = fp.read().split('\n')
                for entry in contents:
                    parsed = entry.split(cls.delimiter)
                    quote_models.append(QuoteModel(parsed[0], parsed[1]))

            return quote_models

        except BaseException:
            raise Exception('Error in ingesting .txt filetype')
