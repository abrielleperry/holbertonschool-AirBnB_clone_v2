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
def states_list(states=None):
    """display a HTML page only if n is an integer"""
    return render_template('9-states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
