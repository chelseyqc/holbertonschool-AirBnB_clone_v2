#!/usr/bin/python3
"""
Starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states_list(id=None):
    """display a HTML page with a list of all State objects"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    specific_state = None

    if id:
        specific_state = next((state for state in states if state.id == id),
                              None)
        if specific_state is not None:
            specific_state.cities = sorted(specific_state.cities,
                                           key=lambda city: city.name)
    elif not states:
        states = []
    return render_template('9-states.html', states=states,
                           specific_state=specific_state)


@app.teardown_appcontext
def teardown_app(exception):
    """removes the current SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
