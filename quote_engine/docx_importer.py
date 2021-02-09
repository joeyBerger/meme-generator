from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel
import docx


class DocxImporter(IngestorInterface):
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path):
        """ Parses text from file, returns quote models """

        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        doc = docx.Document(path)
        quote_models = []
        for p in doc.paragraphs:
            if p.text != "":
                parsed = p.text.split(cls.delimiter)
                quote_models.append(QuoteModel(parsed[0], parsed[1]))

        return quote_models
