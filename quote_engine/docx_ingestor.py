from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel
import docx


class DocxImporter(IngestorInterface):
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path):
        """ Parses text from file, returns quote models """

        if not cls.can_ingest(path):
            raise Exception(f'Problem ingesting .docx file.'
                            f'Please check for correct format/corrupt file.')

        try:
            doc = docx.Document(path)
            quote_models = []
            for p in doc.paragraphs:
                if p.text != "":
                    parsed = p.text.split(cls.delimiter)
                    quote_models.append(QuoteModel(parsed[0], parsed[1]))

            return quote_models

        except BaseException:
            raise Exception('Error in ingesting .docx filetype')
