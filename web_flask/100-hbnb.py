#!/usr/bin/python3
"""
Starts a Flask web application with custom static files and dynamic content
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.teardown_appcontext
def teardown_db(exception):
    """Close the storage on teardown"""
    storage.close()

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Render the HBNB page"""
    states = storage.all("State").values()
    cities = storage.all("City").values()
    amenities = storage.all("Amenity").values()
    places = storage.all("Place").values()
    # Sort by name
    states = sorted(states, key=lambda state: state.name)
    cities = sorted(cities, key=lambda city: city.name)
    amenities = sorted(amenities, key=lambda amenity: amenity.name)
    places = sorted(places, key=lambda place: place.name)
    return render_template('100-hbnb.html', states=states, cities=cities, amenities=amenities, places=places)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

