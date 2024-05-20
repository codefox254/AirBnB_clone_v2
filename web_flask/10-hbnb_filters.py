#!/usr/bin/python3
"""
Starts a Flask web application
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.teardown_appcontext
def teardown_db(exception):
    """Close the storage on teardown"""
    storage.close()

@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Render the filters page"""
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    # Sort states and amenities by name
    states = sorted(states, key=lambda state: state.name)
    amenities = sorted(amenities, key=lambda amenity: amenity.name)
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

