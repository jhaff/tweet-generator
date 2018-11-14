from flask import Flask
from form_sentence import generate_markov_sentence
import split_text_file
from dictogram import Dictogram
from markov_dictogram import Markov_Dictogram

app = Flask(__name__)

@app.route('/')
def hello_world():

    word_list = split_text_file.split_text("huck_finn.txt")

    histogram = Dictogram(word_list)

    markov_histogram = Markov_Dictogram(word_list)

    sentence = generate_markov_sentence(histogram,markov_histogram,20)

    return sentence
