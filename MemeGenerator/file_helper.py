import random


class FileHelper:
    """ Class that helps generate file names """

    @classmethod
    def return_random_file_name(cls):
        """ Generates random number """

        return random.randint(0, 1000000)
