#!/usr/bin/python3
"""flask model"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(close):
    """remove current SQLAlchemy session"""
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_list(id=None):
    """display a HTML page only if n is an integer"""
    states = storage.all("State").values()
    if id is not None:
        state = next((state for state in states if state.id == id), None)
        if state is not None:
            state = [state]
        else:
            state = []
    return render_template('9-states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
