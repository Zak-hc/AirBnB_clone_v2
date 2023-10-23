#!/usr/bin/python3
'''flasck initialisation'''
from flask import *

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def make():
    '''lll'''
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def mako():
    '''lll'''
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def maka(text):
    '''lll'''
    text = text.replace("_", " ")
    return "C " + text


@app.route("/python/<text>", strict_slashes=False)
def maki(text):
    '''lll'''
    text = text.replace("_", " ")
    return "Python " + text


@app.route("/python", strict_slashes=False)
def maku():
    '''lll'''
    return "Python is cool"


@app.route("/number/<int:n>", strict_slashes=False)
def maky(n):
    '''lll'''
    return n + "is a number"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
