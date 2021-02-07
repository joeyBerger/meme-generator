from abc import ABC, abstractmethod

class IngestorInterface(ABC):
    allowed_extensions = []
    delimiter = ' - '

    @classmethod
    def can_ingest(cls, path):
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path):
        pass