# Random Wikipedia Link Generator

This is a simple Flask application that provides a random Wikipedia link. When accessed, it redirects to a random Wikipedia article.

## Features

- **Random Wikipedia Link Endpoint:**
  - The endpoint `/random-wikipedia-link` fetches a random Wikipedia article and returns the URL in JSON format.

- **CORS Enabled:**
  - CORS (Cross-Origin Resource Sharing) is enabled for all routes, allowing requests from other domains.

- **Client-Side Interaction:**
  - The application includes a basic JavaScript snippet that fetches the random Wikipedia link from the Flask server and redirects the browser to the provided URL.

## Prerequisites

- Python 3.x
- `Flask` Python library
- `Flask-CORS` Python library
- `requests` library

## How to Run

1. Clone this repository:

```bash
git clone <repo-link>
```

2. Install the necessary Python libraries:

```bash
pip3 install Flask Flask-CORS requests
```

3. Run the app.py file:

```bash
python app.py
```

4. Run live server
