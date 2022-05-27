## Basic Instructions
- Initiate virtual environment `source venv/bin/activate`
- Command to run in local: `gunicorn --bind 0.0.0.0:5000 wsgi:app -w 1`
- Prod URL: `https://craemy-pie-prod.herokuapp.com`
