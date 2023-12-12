#!/usr/bin/python3
"""
Starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb_display():
    """
    displays "Hello HBNB!"
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_display():
    """
    displays "HBNB"
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def text_display(text):
    """
    displays "C" followed by the value of the text variable
    """
    return "C %s" % text.replace("_", " ")


@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_display(text):
    """
    displays "Python" followed by the value of the text variable
    """
    return "Python %s" % text.replace("_", " ")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
