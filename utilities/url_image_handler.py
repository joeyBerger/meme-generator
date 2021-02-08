from PIL import Image
import shutil
import os
import requests
from .file_helper import FileHelper
import mimetypes

class URLImageHandler:
    dir = './tmp_url_images'
    
    @classmethod
    def save_file(cls,url):

        try:
            img = Image.open(requests.get(url, stream=True).raw)
        except:
            return Exception()

        rand_numb = FileHelper.return_random_file_name()

        try:
            os.mkdir(cls.dir)
        except:
            print("Directory already exists")

        response = requests.get(url)
        content_type = response.headers['content-type']
        ext = mimetypes.guess_extension(content_type)
        file_path = f"{cls.dir}/{rand_numb}.{ext}"

        img.save(file_path)
        return file_path

    @classmethod
    def remove_dir(cls):        
        shutil.rmtree(cls.dir)
