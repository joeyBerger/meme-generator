import random

class FileHelper:

    @classmethod
    def return_random_file_name(cls):
        return random.randint(0,1000000)