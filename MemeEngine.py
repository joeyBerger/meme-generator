from PIL import Image
import os
import random
import shutil

class MemeEngine:
    def __init__(self,output_dir):
        self.output_dir = output_dir

    def make_meme(self,img_path,text,author,width=500):
        # crop = (450, 900, 900, 1300)
        img = Image.open(img_path)

        # img = img.crop(crop)
        ratio = width/float(img.size[0])
        height = int(ratio*float(img.size[1]))
        img = img.resize((width, height), Image.NEAREST)
        
        try:
            shutil.rmtree(self.output_dir)
        except:
            print('No directory to remove.')
            pass

        try:
            os.mkdir(self.output_dir)
        except:
            # raise Exception("Error making new directory for meme image")
            pass

        rand_numb = random.randint(0,1000000)
        file_path = f"{self.output_dir}/{rand_numb}.jpg"
        img.save(file_path)
        return file_path