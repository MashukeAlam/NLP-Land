from flask import Flask
from flask_cors import CORS
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from collections import Counter
from heapq import nlargest

app = Flask(__name__)
CORS(app)

def summarizer(raw):


@app.route('/running')
def running():
    return {"server_running": True}

if __name__ == "__main__":
    app.run(debug=True, port=3333)

