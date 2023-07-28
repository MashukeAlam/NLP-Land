from flask import Flask, request

from flask_cors import CORS
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from collections import Counter
from heapq import nlargest

app = Flask(__name__)
CORS(app)

def summarizer(text, summary_len_cent):
    nlp = spacy.load('en_core_web_sm')

    doc = nlp(text)
    tokens = [token.text for token in doc]

    word_freq = {}

    for word in doc:
        if word.text.lower() not in list(STOP_WORDS) and word.text.lower() not in punctuation:
            if word.text not in word_freq:
                word_freq[word.text] = 1
            else:
                word_freq[word.text] += 1
    
    max_freq = max(word_freq.values())

    for word in word_freq.keys():
        word_freq[word] = word_freq[word] / max_freq

    sent_tokens= [sent for sent in doc.sents]
    sent_scores = dict()
    for sent in sent_tokens:
        for word in sent:
            if word.text.lower() in word_freq.keys():
                if sent not in sent_scores.keys():                            
                    sent_scores[sent] = word_freq[word.text.lower()]
                else:
                    sent_scores[sent] += word_freq[word.text.lower()]

    len_tokens = int(len(sent_tokens)*summary_len_cent)
    summary = nlargest(n = len_tokens, iterable = sent_scores,key=sent_scores.get)
    final_summary=[word.text for word in summary]
    summary=" ".join(final_summary)
    return summary


@app.route('/running')
def running():
    return {"server_running": True}

@app.route('/summary', methods=['POST'])
def summary():
    data = request.form.data
    print(data)

if __name__ == "__main__":
    app.run(debug=True, port=3333)

