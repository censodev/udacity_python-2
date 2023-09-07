import random
import os
import requests
from flask import Flask, render_template, abort, request
from modules.MemeEngine import MemeEngine
from modules.QuoteEngine.ingestor import Ingestor
from utils import build_abs_local_path

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']
    quotes = []
    for file in quote_files:
        for quote in Ingestor.parse(build_abs_local_path(file)):
            quotes.append(quote)

    images_path = build_abs_local_path("./_data/photos/dog/")
    imgs = []
    for root, _, files in os.walk(images_path):
        for file in files:
            imgs.append(os.path.join(root, file))

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """
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
    image_url = request.form.get('image_url')
    img = requests.get(image_url)
    tmp_path = build_abs_local_path('./tmp_img.jpg')
    with open(tmp_path, 'wb') as fo:
        fo.write(img.content)
    body = request.form.get('body')
    author = request.form.get('author')
    path = meme.make_meme(tmp_path, body, author)
    os.remove(tmp_path)
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
