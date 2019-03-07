from flask import Flask
from form_sentence import generate_markov_sentence
from split_text_file import tokenize_text
import split_text_file
from dictogram import Dictogram
from markov_dictogram import Markov_Dictogram
from second_markov_dictogram import Second_Markov_Dictogram


app = Flask(__name__)

@app.route('/')
def hello_world():

    word_list = tokenize_text("huck_finn.txt")

    histogram = Dictogram(word_list)

    markov_histogram = Second_Markov_Dictogram(word_list)

    sentence = generate_markov_sentence(markov_histogram,14)

    return sentence
