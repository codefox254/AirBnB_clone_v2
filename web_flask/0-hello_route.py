#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Display 'Hello HBNB!'"""
    return "Hello HBNB!"

# No blank line at the end of the file
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
