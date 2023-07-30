import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

from flask import Flask, request
from flask_cors import CORS, cross_origin
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
from collections import Counter
from heapq import nlargest

app = Flask(__name__)
CORS(app)
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('vader_lexicon')

def sentimentAnalyzer(text):
    print(f"# Received text: {text}")
    cleaned = text
    cleaned = cleaned.lower()
    cleaned = cleaned.translate(str.maketrans('', '', punctuation))
    tokens = word_tokenize(cleaned)
    without_stops = [token for token in tokens if token not in stopwords.words('english')]

    lemmatizer = WordNetLemmatizer()
    lemmas = [lemmatizer.lemmatize(token) for token in without_stops]

    cleaned = ' '.join(lemmas)
    print(f"# Cleaned text: {cleaned}")

    sia = SentimentIntensityAnalyzer()
    scores = sia.polarity_scores(cleaned)
    print(scores)
    return scores


def textSummarizer(text, percentage):
    
    # load the model into spaCy
    nlp = spacy.load('en_core_web_sm')
    
    # pass the text into the nlp function
    doc= nlp(text)
    
    ## The score of each word is kept in a frequency table
    tokens=[token.text for token in doc]
    freq_of_word=dict()
    
    # Text cleaning and vectorization 
    for word in doc:
        if word.text.lower() not in list(STOP_WORDS):
            if word.text.lower() not in punctuation:
                if word.text not in freq_of_word.keys():
                    freq_of_word[word.text] = 1
                else:
                    freq_of_word[word.text] += 1
                    
    # Maximum frequency of word
    max_freq=max(freq_of_word.values())
    
    # Normalization of word frequency
    for word in freq_of_word.keys():
        freq_of_word[word]=freq_of_word[word]/max_freq
        
    # In this part, each sentence is weighed based on how often it contains the token.
    sent_tokens= [sent for sent in doc.sents]
    sent_scores = dict()
    for sent in sent_tokens:
        for word in sent:
            if word.text.lower() in freq_of_word.keys():
                if sent not in sent_scores.keys():                            
                    sent_scores[sent]=freq_of_word[word.text.lower()]
                else:
                    sent_scores[sent]+=freq_of_word[word.text.lower()]
    
    
    len_tokens=int(len(sent_tokens)*percentage)
    
    # Summary for the sentences with maximum score. Here, each sentence in the list is of spacy.span type
    summary = nlargest(n = len_tokens, iterable = sent_scores,key=sent_scores.get)
    
    # Prepare for final summary
    final_summary=[word.text for word in summary]
    
    #convert to a string
    summary=" ".join(final_summary)
    
    # Return final summary
    return summary

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/running')
def running():
    return {"server_running": True}

@app.route('/summary', methods=['POST'])
@cross_origin(origin='*')
def summary():
    data = request.json['text']
    # print(data)
    return textSummarizer(data, 0.2)

# remove GET in production
@app.route('/sentiment', methods=['POST'])
@cross_origin(origins='*')
def sentiment():
    data = request.json['text']
    return sentimentAnalyzer(data)


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port="3333")
    print("Server started.")

