import json
import random
from flask import Flask, render_template, jsonify
from pathlib import Path

app = Flask(__name__)

# Load countries data
countries_file = Path(__file__).parent / 'static' / 'countries.json'
with open(countries_file, 'r', encoding='utf-8') as f:
    COUNTRIES = json.load(f)


@app.route('/')
def index():
    """Serve the main page"""
    return render_template('index.html')


@app.route('/api/random-country')
def random_country():
    """Return a random country from the list"""
    country = random.choice(COUNTRIES)
    return jsonify(country)


if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)

