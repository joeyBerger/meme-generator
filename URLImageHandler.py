from PIL import Image
import shutil
import urllib3
import random
import os
import requests

class URLImageHandler:
    dir = './tmp_url_images'
    
    @classmethod
    def save_file(cls,url):
        try:
            img = Image.open(requests.get(url, stream=True).raw)
        except:
            return Exception()

        # make this a utility
        rand_numb = random.randint(0,1000000)

        os.mkdir(cls.dir)

        file_path = f"{cls.dir}/{rand_numb}.jpg"
        img.save(file_path)
        return file_path

    @classmethod
    def remove_dir(cls):        
        shutil.rmtree(cls.dir)
