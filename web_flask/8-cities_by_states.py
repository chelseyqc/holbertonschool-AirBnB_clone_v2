#!/usr/bin/python3
"""
Starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """
    displays a HTML page with a list of all State objects and cities
    """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    for state in sorted_states:
        state.cities = sorted(state.cities, key=lambda city: city.name)
    return render_template("8-cities_by_states.html", states=sorted_states)


@app.teardown_appcontext
def teardown_app(exception):
    """removes the current SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
