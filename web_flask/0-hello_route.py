#!/usr/bin/python3
#flasck
from flask import *
app = Flask(__name__)
@app.route("/", strict_slashes=False)
def make():
    '''lll'''
    return "Hello HBNB!"
if __name__ == "__main__":
    app.run(host="0.0.0.0")
