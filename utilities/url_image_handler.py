from PIL import Image
import shutil
import os
import requests
from .file_helper import FileHelper
import mimetypes


class URLImageHandler:
    """ Handles URL input for user generated meme"""

    dir = './tmp_url_images'

    @classmethod
    def save_file(cls, url):
        """ Saves submitted URL image to disk """

        """ Try to open submitted image """
        try:
            img = Image.open(requests.get(url, stream=True).raw)
        except BaseException:
            return Exception()

        rand_numb = FileHelper.return_random_file_name()

        """ Try to make temporary directory """
        try:
            os.mkdir(cls.dir)
        except BaseException:
            print("Directory already exists")

        """ Infer file type """
        response = requests.get(url)
        content_type = response.headers['content-type']
        ext = mimetypes.guess_extension(content_type)
        file_path = f"{cls.dir}/{rand_numb}.{ext}"

        """ Save file to disk """
        img.save(file_path)
        return file_path

    @classmethod
    def remove_dir(cls):
        """ Helper function that removes given directory """

        shutil.rmtree(cls.dir)
