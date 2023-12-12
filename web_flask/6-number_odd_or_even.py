#!/usr/bin/python3
"""
Starts a Flask web application
"""
from flask import Flask, render_template

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


@app.route("/number/<int:n>", strict_slashes=False)
def number_display(n):
    """
    displays n "is a number" only if n is an integer
    """
    return "%i is a number" % n


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    displays a HTML page only if n is an integer
    """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_even(n):
    """
    displays a HTML plage only if n is an integer
    """
    return render_template("6-number_odd_or_even.html", n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
