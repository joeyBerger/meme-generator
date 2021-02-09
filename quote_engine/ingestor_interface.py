from abc import ABC, abstractmethod


class IngestorInterface(ABC):
    """ Abstract interface for varios file ingestors """

    allowed_extensions = []
    delimiter = ' - '

    @classmethod
    def can_ingest(cls, path):
        """ Checks whether file can be ingested """

        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path):
        """ Method that will be realized in inherited classes """

        pass
