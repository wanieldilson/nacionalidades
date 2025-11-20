# Spanish Nationality Learning App

A simple and interactive web application to help you learn Spanish nationality words and their gender forms.

## Features

- Displays random countries with their flags
- Shows country names in Spanish
- Four buttons to reveal nationality forms:
  - **el** - masculine singular
  - **la** - feminine singular
  - **los** - masculine plural
  - **las** - feminine plural
- Beautiful, responsive Bootstrap UI
- 40 different countries to practice with

## Requirements

- Python 3.7 or higher
- Flask 3.0.0

## Installation

1. Clone or download this repository

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the App

1. Start the Flask server:

```bash
python app.py
```

2. Open your web browser and navigate to:

```
http://localhost:5000
```

3. Start learning! Click on the gender buttons (el, la, los, las) to see the nationality word for that form, then click "Siguiente" (Next) to load a new country.

## How to Use

1. A random country will be displayed with its flag
2. The country name appears in Spanish below the flag
3. Click any of the four gender buttons to see the corresponding nationality form:
   - **el** for masculine singular (e.g., "inglés")
   - **la** for feminine singular (e.g., "inglesa")
   - **los** for masculine plural (e.g., "ingleses")
   - **las** for feminine plural (e.g., "inglesas")
4. Click the "Siguiente" button to load a new random country

## Project Structure

```
nacionalidades/
├── app.py                      # Flask application
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── templates/
│   └── index.html             # Main HTML template
└── static/
    └── countries.json         # Country data with nationality forms
```

## Countries Included

The app includes 40 countries from around the world, including:
- European countries (Spain, France, Germany, Italy, etc.)
- American countries (USA, Mexico, Argentina, Brazil, etc.)
- Asian countries (China, Japan, Korea, India, etc.)
- And more!

## Technologies Used

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML5, CSS3, JavaScript
- **UI Framework**: Bootstrap 5
- **Flag Images**: flagcdn.com API
- **Production Server**: Gunicorn

## Running with Docker

### Build the Docker Image

```bash
docker build -t nacionalidades-app .
```

### Run the Docker Container

```bash
docker run -p 5000:5000 -e PORT=5000 nacionalidades-app
```

Then open your browser to `http://localhost:5000`

### Stop the Container

Find the container ID:

```bash
docker ps
```

Stop the container:

```bash
docker stop <container_id>
```

## Deployment to Render

This app is ready to deploy on Render using Docker:

1. Push your code to a GitHub repository

2. Go to [Render Dashboard](https://dashboard.render.com/) and create a new Web Service

3. Connect your GitHub repository

4. Configure the service:
   - **Environment**: Docker
   - **Region**: Choose your preferred region
   - **Branch**: main (or your default branch)
   - Render will automatically detect the Dockerfile

5. Click "Create Web Service"

Render will automatically build and deploy your app. The app will be available at the URL provided by Render.

### Alternative: Deploy without Docker

If you prefer not to use Docker on Render:

1. In Render, select **Python** as the environment instead of Docker
2. Set the following:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn --bind 0.0.0.0:$PORT --workers 2 --threads 4 app:app`

## License

This project is open source and available for educational purposes.

