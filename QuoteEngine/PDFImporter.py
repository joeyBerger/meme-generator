from typing import List
import subprocess
import os
import random

from IngestorInterface import IngestorInterface
from QuoteModel import QuoteModel

class PDFImporter(IngestorInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path):
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')

        # tmp = f'./tmp/{random.randint(0,1000000)}.txt'
        tmp = f'./{random.randint(0,1000000)}.txt'
        subprocess.call(['pdftotext', path, tmp])

        file_ref = open(tmp, "r")
        quote_models = []

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
                        quote_models.append(QuoteModel(body,author))
                    i += 1

        file_ref.close()
        os.remove(tmp)
        return quote_models