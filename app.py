import random
import os
import requests
from flask import Flask, render_template, abort, request

# @TODO Import your Ingestor and MemeEngine classes
from QuoteEngine.Ingestor import Ingestor
from MemeEngine import MemeEngine
from URLImageHandler import URLImageHandler

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # TODO: Use the Ingestor class to parse all files in the
    # quote_files variable
    quotes = None

    images_path = "./_data/photos/dog/"
    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    # img = random.choice(imgs)

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                    './_data/DogQuotes/DogQuotesDOCX.docx',
                    './_data/DogQuotes/DogQuotesPDF.pdf',
                    './_data/DogQuotes/DogQuotesCSV.csv']
    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    # quote = random.choice(quotes)

    # TODO: Use the pythons standard library os class to find all
    # images within the images images_path directory
    # imgs = None
    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    # @TODO:
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    body = request.form['body']
    author = request.form['author']
    image_url = request.form['image_url']

    # image_url = 'https://static01.nyt.com/images/2019/06/17/science/17DOGS/17DOGS-superJumbo.jpg?quality=90&auto=webp'
    # https://post.medicalnewstoday.com/wp-content/uploads/sites/3/2020/02/322868_1100-800x825.jpg

    try:
        img = URLImageHandler.save_file(image_url)
        path = meme.make_meme(img, body, author)
        URLImageHandler.remove_dir()
    except:
        # raise Exception('Error generating meme due to image URL')
        return render_template('meme_form_error.html')

    return render_template('meme.html', path=path)

if __name__ == "__main__":
    app.run()
