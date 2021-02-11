from utilities.file_helper import FileHelper
from PIL import Image, ImageDraw, ImageFont
import os
import shutil


class MemeGenerator:
    """ Set instance attributes """

    def __init__(self, output_dir):
        self.output_dir = output_dir
        self.default_font = './fonts/LilitaOne-Regular.ttf'
        self.default_font_size = 35
        self.text_margins = (25, 35)

    def make_meme(self, img_path, text, author, width=500):
        """ Try to open supplied image, resize and add text to meme """

        if width > 500:
            width = 500

        try:
            img = Image.open(img_path)
        except Exception as e:
            print(e)
            return Exception()

        """ Set aspect ratio of resized image """
        ratio = width / float(img.size[0])
        height = int(ratio * float(img.size[1]))
        img = img.resize((width, height), Image.NEAREST)

        """ Draw body of quote """
        draw = ImageDraw.Draw(img)
        font, w, h = self.generate_suitable_font_with_dimensions(
            draw, width, text)
        draw.text(((width - w) / 2, self.text_margins[1] - h / 2),
                  text, font=font, fill='white')

        """ Draw author of quote """
        draw = ImageDraw.Draw(img)
        font, w, h = self.generate_suitable_font_with_dimensions(
            draw, width, author)
        draw.text(((width - w) / 2, height - (h / 2 + self.text_margins[1])),
                  author, font=font, fill='white')

        """ Try to remove exsisting temporary directory """
        try:
            shutil.rmtree(self.output_dir)
        except Exception as e:
            print(e)

        """ Try to add temporary directory """
        try:
            os.mkdir(self.output_dir)
        except Exception as e:
            print(e)

        """ Generate new file name based on submitted meme extension """
        rand_numb = FileHelper.return_random_file_name()
        file_split = img_path.split('.')
        ext = file_split[-1]

        file_path = f"{self.output_dir}/{rand_numb}.{ext}"

        """ Try to save generated meme """
        try:
            img.save(file_path)
        except Exception as e:
            print(e)

        """ Return meme's file path """
        return file_path

    def generate_suitable_font_with_dimensions(self, draw, width, message):
        """ Function that tries to fit text into given meme
            dimensions by continually reducing font size until text fits
            within given margins
        """

        font = ImageFont.truetype(self.default_font, size=35)
        w, h = draw.textsize(message, font=font)
        for i in range(self.default_font_size - 1):
            if width - w < self.text_margins[0]:
                font = ImageFont.truetype(self.default_font, size=35 - (i + 1))
                w, h = draw.textsize(message, font=font)
        return font, w, h
