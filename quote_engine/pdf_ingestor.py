from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel
import subprocess
import os
import random


class PDFImporter(IngestorInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path):
        """ Parses text from file, returns quote models """

        if not cls.can_ingest(path):
            raise Exception(f'Problem ingesting .pdf file.'
                            f'Please check for correct format/corrupt file.')

        try:
            """ create new temp text file for storage of PDF text"""
            tmp = f'./{random.randint(0,1000000)}.txt'
            subprocess.call(['pdftotext', path, tmp])

            file_ref = open(tmp, "r")
            quote_models = []

            """ parse text to quote model """
            for line in file_ref.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parsed = line.split('"')
                    i = 0
                    for _ in parsed:
                        if i < len(parsed) and parsed[i] != '':
                            body = parsed[i]
                            i += 1
                            author = parsed[i]
                            quote_models.append(QuoteModel(body, author))
                        i += 1

            file_ref.close()
            os.remove(tmp)
            return quote_models

        except BaseException:
            raise Exception('Error in ingesting .pdf filetype')
